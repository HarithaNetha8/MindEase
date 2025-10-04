import React, { useState } from 'react';

type MoodEntry = { mood: string; at: string };

const STORAGE_KEY = 'mindease:mood_history_v1';

const MoodTracker: React.FC = () => {
  const [mood, setMood] = useState('');
  const [history, setHistory] = useState<MoodEntry[]>(() => {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) as MoodEntry[] : [];
    } catch {
      return [];
    }
  });

  const saveHistory = (next: MoodEntry[]) => {
    setHistory(next);
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(next)); } catch {}
  };

  const submitMood = () => {
    if (!mood) return;
    const entry: MoodEntry = { mood, at: new Date().toISOString() };
    saveHistory([entry, ...history].slice(0, 50));
    setMood('');
  };

  const clearHistory = () => {
    saveHistory([]);
  };

  return (
    <div>
      <h2>Mood Tracker</h2>
      <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
        <select value={mood} onChange={e => setMood(e.target.value)} style={{ flex: 1 }}>
          <option value="">Select your mood</option>
          <option value="😊 Happy">😊 Happy</option>
          <option value="😔 Sad">😔 Sad</option>
          <option value="� Angry">� Angry</option>
          <option value="😴 Tired">😴 Tired</option>
        </select>
        <button onClick={submitMood}>Save</button>
      </div>

      <div style={{ marginTop: 12 }}>
        <h4 style={{ marginBottom: 6 }}>Recent</h4>
        {history.length === 0 && <div style={{ color: '#666' }}>No moods yet.</div>}
        <ul style={{ paddingLeft: 18 }}>
          {history.map((h, i) => (
            <li key={h.at + i} style={{ marginBottom: 6 }}>
              <strong>{h.mood}</strong> <span style={{ color: '#888', fontSize: 12 }}>— {new Date(h.at).toLocaleString()}</span>
            </li>
          ))}
        </ul>

        {history.length > 0 && (
          <button onClick={clearHistory} style={{ marginTop: 8, color: '#a00' }}>Clear history</button>
        )}
      </div>
    </div>
  );
};

export default MoodTracker;
