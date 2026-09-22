import { useMemo, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const initialMessages = [
  {
    id: "welcome",
    role: "assistant",
    content: "Tiffbot online. What are we building, solving, or exploring today?",
  },
];

function App() {
  const [messages, setMessages] = useState(initialMessages);
  const [draft, setDraft] = useState("");
  const [sessionId, setSessionId] = useState(null);
  const [isSending, setIsSending] = useState(false);
  const [error, setError] = useState("");

  const messageCount = useMemo(() => messages.length, [messages]);

  async function sendMessage(event) {
    event.preventDefault();
    const message = draft.trim();
    if (!message || isSending) return;

    setMessages((current) => [
      ...current,
      { id: `${Date.now()}-user`, role: "user", content: message },
    ]);
    setDraft("");
    setError("");
    setIsSending(true);

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, session_id: sessionId }),
      });

      if (!response.ok) throw new Error("The Tiffbot API is not available.");

      const data = await response.json();
      setSessionId(data.session_id);
      setMessages((current) => [
        ...current,
        {
          id: `${Date.now()}-assistant`,
          role: "assistant",
          content: data.reply,
        },
      ]);
    } catch (requestError) {
      setError(requestError.message);
      setMessages((current) => [
        ...current,
        {
          id: `${Date.now()}-error`,
          role: "assistant",
          content: "I could not reach the execution layer. Check that the API is running, then try again.",
        },
      ]);
    } finally {
      setIsSending(false);
    }
  }

  return (
    <main className="app-shell">
      <aside className="rail">
        <div className="brand-mark" aria-label="Tiffbot home">T</div>
        <div className="rail-status"><span className="status-dot" /> Ready</div>
      </aside>

      <section className="workspace">
        <header className="topbar">
          <div>
            <p className="eyebrow">Tiff / Core assistant</p>
            <h1>Tiffbot</h1>
          </div>
          <div className="system-state">
            <span className="pulse" /> Super Computer connected
          </div>
        </header>

        <div className="content-grid">
          <section className="conversation-panel" aria-label="Tiffbot conversation">
            <div className="conversation-head">
              <div>
                <p className="eyebrow">One continuous thread</p>
                <h2>Let&apos;s make it real.</h2>
              </div>
              <span className="message-count">{messageCount} messages</span>
            </div>

            <div className="messages" aria-live="polite">
              {messages.map((message) => (
                <article className={`message ${message.role}`} key={message.id}>
                  <span className="message-label">{message.role === "assistant" ? "Tiffbot" : "You"}</span>
                  <p>{message.content}</p>
                </article>
              ))}
              {isSending && <div className="typing-indicator"><span /><span /><span /> Thinking</div>}
            </div>

            <form className="composer" onSubmit={sendMessage}>
              <textarea
                value={draft}
                onChange={(event) => setDraft(event.target.value)}
                onKeyDown={(event) => {
                  if (event.key === "Enter" && !event.shiftKey) {
                    event.preventDefault();
                    event.currentTarget.form.requestSubmit();
                  }
                }}
                placeholder="Ask Tiffbot to help, research, or execute..."
                rows="1"
                aria-label="Message Tiffbot"
              />
              <button type="submit" disabled={!draft.trim() || isSending} aria-label="Send message">
                <span>Send</span>
                <span aria-hidden="true">↗</span>
              </button>
            </form>
            {error && <p className="error-text">{error}</p>}
            <p className="composer-hint">Enter to send · Shift + Enter for a new line</p>
          </section>

          <aside className="capability-panel" aria-label="Tiffbot capabilities">
            <p className="eyebrow">Capabilities</p>
            <h3>From intent to outcome.</h3>
            <p className="capability-copy">Tiffbot decides what the request needs. You stay in the thread.</p>
            <div className="capability-list">
              <div className="capability-item active"><span>01</span><strong>Chat</strong><small>Think together</small></div>
              <div className="capability-item"><span>02</span><strong>Research</strong><small>Find the signal</small></div>
              <div className="capability-item"><span>03</span><strong>Images</strong><small>Make it visual</small></div>
              <div className="capability-item"><span>04</span><strong>Super Computer</strong><small>Actually do it</small></div>
            </div>
            <div className="operator-note"><span className="note-icon">✦</span><p>Built for the next move, not just the next answer.</p></div>
          </aside>
        </div>
      </section>
    </main>
  );
}

export default App;
