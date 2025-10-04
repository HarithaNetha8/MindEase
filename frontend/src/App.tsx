import React from 'react'
import Chatbot from './components/Chatbot'
import MoodTracker from './components/MoodTracker'

const App: React.FC = () => {
  return (
    <div style={{ maxWidth: 900, margin: '40px auto', padding: 16 }}>
      <header style={{ textAlign: 'center', marginBottom: 24 }}>
        <h1>MindEase - AI Mental Wellness Companion</h1>
        <p>Chat with our AI assistant for emotional support and track your mood.</p>
      </header>

      <main style={{ display: 'grid', gridTemplateColumns: '1fr 380px', gap: 24 }}>
        <section>
          <Chatbot />
        </section>

        <aside style={{ borderLeft: '1px solid #eee', paddingLeft: 16 }}>
          <MoodTracker />
        </aside>
      </main>
    </div>
  )
}

export default App
