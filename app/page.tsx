'use client';
import { useState, useEffect } from 'react';

export default function Home() {
  const [pincode, setPincode] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [isDark, setIsDark] = useState(false);

  useEffect(() => {
    if (typeof window !== 'undefined' && window.matchMedia) {
      setIsDark(window.matchMedia('(prefers-color-scheme: dark)').matches);
    }
  }, []);

  const fetchPlumbers = async () => {
    setLoading(true);
    setResult('');
    try {
      const res = await fetch('http://127.0.0.1:8000/get-plumbers', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pincode }),
      });
      const data = await res.json();
      setResult(data.result);
    } catch (e) {
      setResult('Error: Failed to fetch data from backend.');
    }
    setLoading(false);
  };

  // Dynamic color styles for light/dark mode
  const resultBoxStyle = {
    marginTop: 24,
    background: isDark ? '#222' : '#f4f4f4',
    color: isDark ? '#fff' : '#222',
    padding: 16,
    borderRadius: 8,
    minHeight: 80,
    wordBreak: 'break-word' as const,
    boxShadow: '0 2px 8px rgba(0,0,0,0.05)',
    transition: 'background 0.3s, color 0.3s'
  };

  return (
    <main
      style={{
        maxWidth: 500,
        margin: 'auto',
        padding: 24,
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        background: isDark ? '#181818' : '#fff',
        transition: 'background 0.3s'
      }}
    >
      <h1 style={{
        fontSize: 28,
        fontWeight: 700,
        marginBottom: 24,
        color: isDark ? '#fff' : '#181818',
        textAlign: 'center'
      }}>
        Find Top Plumbers by Pincode
      </h1>
      <input
        type="text"
        placeholder="Enter pincode"
        value={pincode}
        onChange={e => setPincode(e.target.value)}
        style={{
          padding: 12,
          width: '100%',
          marginBottom: 16,
          fontSize: 16,
          borderRadius: 6,
          border: '1px solid #ccc',
          outline: 'none',
          boxSizing: 'border-box'
        }}
      />
      <button
        onClick={fetchPlumbers}
        disabled={loading || !pincode}
        style={{
          padding: 12,
          width: '100%',
          fontSize: 16,
          borderRadius: 6,
          background: loading || !pincode ? '#aaa' : '#0070f3',
          color: '#fff',
          border: 'none',
          cursor: loading || !pincode ? 'not-allowed' : 'pointer',
          fontWeight: 600,
          marginBottom: 16,
          transition: 'background 0.2s'
        }}
      >
        {loading ? 'Searching...' : 'Find Plumbers'}
      </button>
      <pre style={resultBoxStyle}>{result}</pre>
    </main>
  );
}