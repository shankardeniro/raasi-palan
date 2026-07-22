import { useState, useEffect, useRef, useCallback, useMemo } from 'react'
import './App.css'

/* ── Data ── */
const SYMBOLS = ['♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒','♓']
const EN = ['Mesha','Rishabha','Mithuna','Kataka','Simha','Kanni','Thulam','Viruchigam','Dhanus','Makara','Kumbha','Meena']
const TA = ['மேஷம்','ரிஷபம்','மிதுனம்','கடகம்','சிம்மம்','கன்னி','துலாம்','விருச்சிகம்','தனுசு','மகரம்','கும்பம்','மீனம்']

/* ── Persistence helpers ── */
function saved(key, fallback) {
  try { const v = localStorage.getItem(key); return v !== null ? v : fallback }
  catch { return fallback }
}

function persist(key, val) {
  try { localStorage.setItem(key, val) } catch {}
}

function formatDate(dateStr, lang) {
  const d = new Date(dateStr + 'T00:00:00')
  const opts = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
  return d.toLocaleDateString(lang === 'ta' ? 'ta-IN' : 'en-IN', opts)
}

/* ═══════════════════════════════════════
   App
   ═══════════════════════════════════════ */
export default function App() {
  const [lang, setLang] = useState(() => saved('raasi-lang', 'ta'))
  const [raasi, setRaasi] = useState(() => {
    const v = saved('raasi-idx', null)
    return v !== null ? parseInt(v, 10) : null
  })
  const [reading, setReading] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const ta = lang === 'ta'

  const switchLang = useCallback((l) => { setLang(l); persist('raasi-lang', l) }, [])

  const confirmRaasi = useCallback((idx) => {
    setRaasi(idx)
    persist('raasi-idx', idx)
  }, [])

  const changeRaasi = useCallback(() => {
    setRaasi(null)
    setReading(null)
    try { localStorage.removeItem('raasi-idx') } catch {}
  }, [])

  useEffect(() => {
    if (raasi === null) return
    setLoading(true)
    setError(null)
    fetch(`/api/reading/${raasi}?lang=${lang}`)
      .then(r => { if (!r.ok) throw new Error('Failed'); return r.json() })
      .then(d => { setReading(d); setLoading(false) })
      .catch(e => { setError(e.message); setLoading(false) })
  }, [raasi, lang])

  /* ── Render ── */
  if (raasi === null) {
    return (
      <Onboard ta={ta} lang={lang} switchLang={switchLang} onConfirm={confirmRaasi} />
    )
  }

  return (
    <>
      <div className="reading-topbar">
        <button className={`change-raasi-btn ${ta ? 'tamil' : ''}`} onClick={changeRaasi}>
          {ta ? 'ராசி மாற்று' : 'Change raasi'}
        </button>
        <LangPill lang={lang} switchLang={switchLang} />
      </div>

      {loading ? (
        <div className="loading">
          <div className="spinner" />
          <span className={ta ? 'tamil' : ''}>{ta ? 'பலன் வருகிறது...' : 'Loading...'}</span>
        </div>
      ) : error ? (
        <div className="error-msg">{error}</div>
      ) : reading ? (
        <ReadingView reading={reading} raasi={raasi} lang={lang} ta={ta} />
      ) : null}

      <footer className={`app-footer ${ta ? 'tamil' : ''}`}>
        {ta ? 'கோசார அடிப்படையிலான தினசரி பலன் · லாகிரி அயனாம்சம்' : 'Daily Gochara transit readings · Lahiri ayanamsa'}
      </footer>
    </>
  )
}

/* ═══════════════════════════════════════
   Onboarding — Wheel Picker
   ═══════════════════════════════════════ */
function Onboard({ ta, lang, switchLang, onConfirm }) {
  const ITEM_H = 56
  const scrollRef = useRef(null)
  const [selected, setSelected] = useState(0)

  /* On scroll, figure out which item is centered */
  const onScroll = useCallback(() => {
    const el = scrollRef.current
    if (!el) return
    const idx = Math.round(el.scrollTop / ITEM_H)
    setSelected(Math.max(0, Math.min(11, idx)))
  }, [])

  /* Initial scroll to first item (centered) */
  useEffect(() => {
    const el = scrollRef.current
    if (el) el.scrollTop = 0
  }, [])

  return (
    <div className="onboard">
      <div className="onboard-lang">
        <button className={`onboard-lang-btn ${lang === 'ta' ? 'active' : ''}`} onClick={() => switchLang('ta')}>தமிழ்</button>
        <button className={`onboard-lang-btn ${lang === 'en' ? 'active' : ''}`} onClick={() => switchLang('en')}>EN</button>
      </div>

      <h1 className={`onboard-title ${ta ? 'tamil' : ''}`}>
        {ta ? 'உங்கள் ஜன்ம ராசி\nஎன்ன?' : 'What is your\nJanma Raasi?'}
      </h1>

      <div className="wheel-wrapper">
        <div className="wheel-fade-top" />
        <div className="wheel-fade-bottom" />
        <div className="wheel-highlight" />
        <div className="wheel-scroll" ref={scrollRef} onScroll={onScroll}>
          <div className="wheel-spacer" />
          {EN.map((name, i) => (
            <div key={i} className={`wheel-item ${i === selected ? 'selected' : ''}`}>
              <span className="wi-symbol">{SYMBOLS[i]}</span>
              <span className={`wi-name ${ta ? 'tamil' : ''}`}>{ta ? TA[i] : name}</span>
              <span className={`wi-sub ${ta ? '' : 'tamil'}`}>{ta ? name : TA[i]}</span>
            </div>
          ))}
          <div className="wheel-spacer" />
        </div>
      </div>

      <button className={`confirm-btn ${ta ? 'tamil' : ''}`} onClick={() => onConfirm(selected)}>
        {ta ? 'பலன் பார்க்க' : 'See my reading'}
      </button>
    </div>
  )
}

/* ═══════════════════════════════════════
   Reading View — Score + Narrative
   ═══════════════════════════════════════ */
function ReadingView({ reading, raasi, lang, ta }) {
  const score = reading.score ?? 5
  const [showToast, setShowToast] = useState(false)

  /* Score color */
  const scoreColor = score >= 7 ? 'var(--good)' : score >= 4 ? 'var(--accent)' : 'var(--caution)'

  /* SVG ring math */
  const R = 42, C = 2 * Math.PI * R
  const offset = C - (score / 10) * C

  const verdict = reading.verdict ?? ''

  /* Compose share text */
  const shareText = useMemo(() => {
    const name = ta ? TA[raasi] : EN[raasi]
    const date = formatDate(reading.date, lang)
    const url = window.location.origin
    return ta
      ? `${SYMBOLS[raasi]} ${name} — ${date}\n\n📊 ${score}/10 — ${verdict}\n\n${reading.narrative}\n\n${url}`
      : `${SYMBOLS[raasi]} ${name} — ${date}\n\n📊 ${score}/10 — ${verdict}\n\n${reading.narrative}\n\n${url}`
  }, [reading, raasi, lang, ta, score, verdict])

  const handleShare = useCallback(async () => {
    if (navigator.share) {
      try {
        await navigator.share({ text: shareText })
        return
      } catch {}
    }
    try {
      await navigator.clipboard.writeText(shareText)
      setShowToast(true)
      setTimeout(() => setShowToast(false), 2000)
    } catch {}
  }, [shareText])

  return (
    <>
      {/* Hero */}
      <div className="reading-hero">
        <div className={`reading-raasi ${ta ? 'tamil' : ''}`}>
          {SYMBOLS[raasi]} {ta ? TA[raasi] : EN[raasi]}
        </div>
        <div className={`reading-date ${ta ? 'tamil' : ''}`}>
          {formatDate(reading.date, lang)}
        </div>
      </div>

      {/* Narrative */}
      <div className="narrative-section">
        <div className="narrative-block">
          <p className={ta ? 'tamil' : ''}>
            {reading.narrative}
          </p>
        </div>
      </div>

      {/* Score + verdict + share — bottom */}
      <div className="score-bottom">
        <div className="score-ring">
          <svg width="80" height="80" viewBox="0 0 100 100">
            <circle className="score-ring-bg" cx="50" cy="50" r={R} />
            <circle
              className="score-ring-fill"
              cx="50" cy="50" r={R}
              stroke={scoreColor}
              strokeDasharray={C}
              strokeDashoffset={offset}
            />
          </svg>
          <div className="score-value">{score}<span className="score-of">/10</span></div>
        </div>
        <div className={`score-verdict ${ta ? 'tamil' : ''}`}>
          {verdict}
        </div>
        <button className="share-btn" onClick={handleShare} aria-label="Share">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/>
            <polyline points="16 6 12 2 8 6"/>
            <line x1="12" y1="2" x2="12" y2="15"/>
          </svg>
        </button>
      </div>

      {/* Toast */}
      <div className={`toast ${showToast ? 'show' : ''}`}>
        {ta ? 'நகலெடுக்கப்பட்டது!' : 'Copied to clipboard!'}
      </div>
    </>
  )
}

/* ── Shared: Language pill ── */
function LangPill({ lang, switchLang }) {
  return (
    <div className="lang-pill">
      <button className={`lang-pill-btn ${lang === 'ta' ? 'active' : ''}`} onClick={() => switchLang('ta')}>தமிழ்</button>
      <button className={`lang-pill-btn ${lang === 'en' ? 'active' : ''}`} onClick={() => switchLang('en')}>EN</button>
    </div>
  )
}
