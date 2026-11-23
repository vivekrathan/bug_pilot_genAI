
import { useState } from "react";
import {
  Bug, LayoutDashboard, History, Settings, Search,
  Bell, Sparkles, AlertTriangle, CheckCircle,
  Activity, Code, Loader2, ChevronRight
} from "lucide-react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [form, setForm] = useState({
    title: "",
    description: "",
    stack_trace: "",
    environment: "",
    component: ""
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function analyzeBug(e) {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/triage`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });

      if (!response.ok) {
        const message = await response.text();
        throw new Error(message || `Server error: ${response.status}`);
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(
        "Unable to analyze this bug. Check that your FastAPI backend is running at " +
        API_URL + ". Details: " + err.message
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-icon"><Bug size={23} /></div>
          <div>
            <h2>BugPilot</h2>
            <span>INTELLIGENT DEBUGGING</span>
          </div>
        </div>

        <div className="nav-label">WORKSPACE</div>
        <div className="nav-item active">
          <LayoutDashboard size={18} /> Dashboard
        </div>
       
       

        <div className="sidebar-bottom">
          <div className="status-dot"></div>
          <div>
            <strong>System status</strong>
            <span>Ready to analyze</span>
          </div>
        </div>
      </aside>

      <main className="main">
        <header className="topbar">
          <div className="breadcrumb">
            Workspace <ChevronRight size={15} /> Dashboard
          </div>
          <div className="top-actions">
            <button className="icon-button"><Search size={19} /></button>
            <button className="icon-button"><Bell size={19} /></button>
            <div className="avatar">VR</div>
          </div>
        </header>

        <section className="content">
          <div className="welcome">
            <div>
              <div className="eyebrow"><Sparkles size={14} /> GENAI-POWERED BUG ANALYSIS</div>
              <h1>Bug Triage Dashboard</h1>
              <p>Understand bugs faster. Find root causes. Ship better software.</p>
            </div>
            <div className="date-chip"><Activity size={16} /> AI ENGINE READY</div>
          </div>


          <div className="section-heading">
            <div>
              <h2>Submit a bug report</h2>
              <p>Describe the issue and let BugPilot investigate it.</p>
            </div>
            <span className="required-label">* Required fields</span>
          </div>

          <div className="workspace-grid">
            <form className="bug-form" onSubmit={analyzeBug}>
              <div className="form-title">
                <div className="form-title-icon"><Code size={19} /></div>
                <div><h3>Bug information</h3><p>Provide details about the problem</p></div>
              </div>

              <label>Bug title <span>*</span></label>
              <input
                name="title"
                value={form.title}
                onChange={handleChange}
                placeholder="e.g. Application crashes during login"
                required
                minLength={3}
              />

              <label>Description <span>*</span></label>
              <textarea
                name="description"
                value={form.description}
                onChange={handleChange}
                placeholder="Explain what happened, what you expected, and how to reproduce the issue..."
                rows={5}
                required
                minLength={5}
              />

              <label>Stack trace <small>(Optional)</small></label>
              <textarea
                className="code-input"
                name="stack_trace"
                value={form.stack_trace}
                onChange={handleChange}
                placeholder="Paste your error message or stack trace..."
                rows={4}
              />

              <div className="two-columns">
                <div>
                  <label>Environment</label>
                  <input
                    name="environment"
                    value={form.environment}
                    onChange={handleChange}
                    placeholder="e.g. Windows, Python 3.12"
                  />
                </div>
                <div>
                  <label>Component</label>
                  <input
                    name="component"
                    value={form.component}
                    onChange={handleChange}
                    placeholder="e.g. Authentication"
                  />
                </div>
              </div>

              {error && <div className="error-message">{error}</div>}

              <button className="analyze-button" type="submit" disabled={loading}>
                {loading ? <Loader2 className="spin" size={19} /> : <Sparkles size={19} />}
                {loading ? "Analyzing bug..." : "Analyze with BugPilot"}
              </button>
              <p className="privacy-note">AI-generated suggestions should be reviewed before applying fixes.</p>
            </form>

            <section className="result-panel">
              <div className="result-heading">
                <div><Sparkles size={19} /><h3>AI Analysis</h3></div>
                <span>LIVE RESULTS</span>
              </div>

              {!result && !loading && (
                <div className="empty-result">
                  <div className="empty-icon"><Bug size={34} /></div>
                  <h3>Ready when you are</h3>
                  <p>Submit a bug report to receive AI-powered severity assessment, root-cause hypotheses and debugging recommendations.</p>
                  <div className="result-feature"><CheckCircle size={16} /> Severity classification</div>
                  <div className="result-feature"><CheckCircle size={16} /> Root-cause hypotheses</div>
                  <div className="result-feature"><CheckCircle size={16} /> Suggested debugging steps</div>
                  <div className="result-feature"><CheckCircle size={16} /> Similar issue retrieval</div>
                </div>
              )}

              {loading && (
                <div className="loading-state">
                  <Loader2 className="spin" size={34} />
                  <h3>Investigating your bug...</h3>
                  <p>BugPilot is analyzing the report.</p>
                </div>
              )}

              {result && (
                <div className="analysis-results">
                  <div className="result-summary">
                    <span>SUMMARY</span>
                    <p>{result.summary}</p>
                  </div>

                  <div className="severity-card">
                    <div><span>DETECTED SEVERITY</span><h2>{result.severity}</h2></div>
                    <AlertTriangle size={25} />
                    <p>{result.severity_reason}</p>
                  </div>

                  <div className="result-block">
                    <h4>Affected subsystem</h4>
                    <p>{result.affected_subsystem}</p>
                  </div>

                  <div className="result-block">
                    <h4>Root cause hypotheses</h4>
                    <ul>{(result.root_cause_hypotheses || []).map((item, i) => <li key={i}>{item}</li>)}</ul>
                  </div>

                  <div className="result-block">
                    <h4>Debugging steps</h4>
                    <ol>{(result.debugging_steps || []).map((item, i) => <li key={i}>{item}</li>)}</ol>
                  </div>

                  <div className="result-block">
                    <h4>Suggested fix</h4>
                    <p>{result.suggested_fix}</p>
                  </div>

                  <div className="result-block">
                    <h4>Similar issues</h4>
                    {(result.similar_issues || []).length === 0
                      ? <p>No similar issues retrieved.</p>
                      : result.similar_issues.map((issue, i) => (
                        <div className="similar-issue" key={issue.id || i}>
                          <strong>{issue.title}</strong>
                          <p>{issue.source} · Similarity: {issue.similarity}</p>
                        </div>
                      ))}
                  </div>

                  <div className="result-block">
                    <h4>Confidence</h4>
                    <p>{result.confidence}</p>
                  </div>

                  {result.limitations?.length > 0 && (
                    <div className="result-block">
                      <h4>Limitations</h4>
                      <ul>{result.limitations.map((item, i) => <li key={i}>{item}</li>)}</ul>
                    </div>
                  )}
                </div>
              )}
            </section>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
