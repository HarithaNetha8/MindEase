import React, { useState } from 'react';

const Chatbot: React.FC = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    const text = input.trim();
    if (!text) return;

    // Add user message
    setMessages(prev => [...prev, `You: ${text}`]);
    setInput('');
    setLoading(true);

    try {
      // Call backend API - use /api/analyze to match backend
      const res = await fetch('http://127.0.0.1:5000/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text }),
      });

      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err?.error || `Server error: ${res.status}`);
      }

      const data = await res.json();
      console.debug('analyze response', data);
      // Include label and score for debugging so it's clear why the bot replied
      const meta = data.label ? ` [${data.label} ${Number(data.score).toFixed(2)}]` : '';
      setMessages(prev => [...prev, `AI: ${data.reply || 'No reply'}${meta}`]);
    } catch (error) {
      console.error(error);
      setMessages(prev => [...prev, '⚠️ Error connecting to server']);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Chatbot</h2>
      <div className="chat-box" style={{ minHeight: 140, border: '1px solid #ddd', padding: 10 }}>
        {messages.length === 0 && <p style={{ color: '#666' }}>Say hi to get started.</p>}
        {messages.map((msg, idx) => (
          <p key={idx} style={{ margin: '6px 0' }}>{msg}</p>
        ))}
      </div>
      <div className="input-box" style={{ marginTop: 8 }}>
        <input 
          value={input} 
          onChange={e => setInput(e.target.value)} 
          placeholder="Type a message..."
          onKeyDown={e => { if (e.key === 'Enter') sendMessage(); }}
          style={{ padding: '8px', width: '70%' }}
          disabled={loading}
        />
        <button onClick={sendMessage} disabled={loading} style={{ marginLeft: 8 }}>
          {loading ? 'Sending...' : 'Send'}
        </button>
      </div>
    </div>
  );
};

export default Chatbot;
