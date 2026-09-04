import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [code, setCode] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeCode = async () => {
    if (!code.trim()) {
      setError("Please paste some code first.");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setResult(null);

      const response = await axios.post(
        "http://127.0.0.1:8000/analyze",
        {
          code: code,
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error("Error analyzing code:", error);
      setError("Failed to analyze the code. Make sure the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <div>
          <p className="eyebrow">CODE AUTHENTICITY ANALYSIS</p>
          <h1>AI Forensics</h1>
          <p className="subtitle">
            Analyze code using machine learning and forensic indicators.
          </p>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          System Online
        </div>
      </header>

      <main className="dashboard">
        <section className="input-section">
          <div className="section-header">
            <div>
              <h2>Code Input</h2>
              <p>Paste the code you want to analyze.</p>
            </div>

            <span className="character-count">
              {code.length} characters
            </span>
          </div>

          <textarea
            placeholder="Paste your code here..."
            value={code}
            onChange={(e) => setCode(e.target.value)}
          />

          <button
            className="analyze-button"
            onClick={analyzeCode}
            disabled={loading}
          >
            {loading ? "Analyzing..." : "Analyze Code"}
          </button>

          {error && (
            <p className="error-message">
              {error}
            </p>
          )}
        </section>

        {result && (
          <>
            <section className="result-section">
              <div className="section-header">
                <div>
                  <h2>Analysis Result</h2>
                  <p>Machine learning classification result.</p>
                </div>
              </div>

              <div className="result-cards">
                <div className="prediction-card">
                  <span>Prediction</span>
                  <strong>{result.prediction}</strong>
                </div>

                <div className="confidence-card">
                  <span>Confidence</span>
                  <strong>{result.confidence}%</strong>

                  <div className="confidence-bar">
                    <div
                      className="confidence-fill"
                      style={{
                        width: `${result.confidence}%`,
                      }}
                    ></div>
                  </div>
                </div>
              </div>
            </section>

            <section className="probabilities-section">
              <div className="section-header">
                <div>
                  <h2>Class Probabilities</h2>
                  <p>Confidence distribution across all categories.</p>
                </div>
              </div>

              <div className="probabilities-list">
                {Object.entries(result.probabilities).map(
                  ([label, probability]) => (
                    <div className="probability-item" key={label}>
                      <div className="probability-top">
                        <span>{label}</span>
                        <strong>{probability}%</strong>
                      </div>

                      <div className="probability-bar">
                        <div
                          className="probability-fill"
                          style={{
                            width: `${probability}%`,
                          }}
                        ></div>
                      </div>
                    </div>
                  )
                )}
              </div>
            </section>

            <section className="forensic-section">
              <div className="section-header">
                <div>
                  <h2>Forensic Analysis</h2>
                  <p>Structural characteristics detected in the submitted code.</p>
                </div>
              </div>

              <div className="metrics-grid">
                {Object.entries(result.forensic_analysis).map(
                  ([metric, value]) => (
                    <div className="metric-card" key={metric}>
                      <span>
                        {metric.replaceAll("_", " ")}
                      </span>

                      <strong>{value}</strong>
                    </div>
                  )
                )}
              </div>
            </section>
          </>
        )}
      </main>
    </div>
  );
}

export default App;