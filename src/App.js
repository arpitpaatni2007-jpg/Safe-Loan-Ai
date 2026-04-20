import React, { useState } from "react";
import axios from "axios";
import { FaExclamationTriangle } from "react-icons/fa";

function App() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
  if (!file) {
    alert("Please select a file!");
    return;
  }

  try {
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(
      "http://127.0.0.1:5001/analyze",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
        timeout: 10000, // prevents hanging
      }
    );

    console.log("RESPONSE:", res.data); // 🔥 debug
    setData(res.data);

  } catch (err) {
    console.error("FULL ERROR:", err);

    if (err.response) {
      alert("Backend responded with error");
    } else if (err.request) {
      alert("No response from backend (check Flask)");
    } else {
      alert("Request error");
    }

  } finally {
    setLoading(false);
  }
};
  // 🎨 Risk color
  const getColor = (risk) => {
    if (risk === "HIGH") return "#ff4d4f";
    if (risk === "MEDIUM") return "#faad14";
    return "#52c41a";
  };

  // 🔥 Highlight keywords
  const highlight = (text, keywords) => {
    let highlighted = text;
    keywords.forEach((word) => {
      const regex = new RegExp(`(${word})`, "gi");
      highlighted = highlighted.replace(
        regex,
        `<span style="color:red;font-weight:bold">$1</span>`
      );
    });
    return highlighted;
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>💰 SafeLoan AI</h1>
        <p style={styles.subtitle}>AI-powered Loan Risk Analyzer</p>

        {/* Upload */}
        <div style={styles.uploadBox}>
          <input type="file" onChange={(e) => setFile(e.target.files[0])} />
          <button style={styles.button} onClick={handleUpload}>
            Analyze
          </button>
        </div>

        {loading && <p style={{ marginTop: 20 }}>⏳ Processing...</p>}

        {/* Results */}
        {data && (
          <>
            <h3>📄 Extracted Text</h3>
            <p style={styles.text}>{data.text}</p>

            {/* Risk Meter */}
            <h3>⚠ Risk Score: {data.score}/100</h3>
            <div style={styles.meter}>
              <div
                style={{
                  ...styles.meterFill,
                  width: `${data.score}%`,
                  background:
                    data.score > 70
                      ? "#ff4d4f"
                      : data.score > 40
                      ? "#faad14"
                      : "#52c41a",
                }}
              />
            </div>

            {/* Overall */}
            <h3>
              Overall Risk:{" "}
              <span style={{ color: getColor(data.overall_risk.split(" ")[0]) }}>
                {data.overall_risk}
              </span>
            </h3>

            <h2 style={{ marginTop: 30 }}>🚨 Detected Risks</h2>

            {data.risks.map((r, i) => (
              <div
                key={i}
                style={{
                  ...styles.riskCard,
                  borderLeft: `6px solid ${getColor(r.risk)}`,
                }}
              >
                <p
                  dangerouslySetInnerHTML={{
                    __html: highlight(r.sentence, r.keywords),
                  }}
                />

                <p style={{ color: getColor(r.risk), fontWeight: "bold" }}>
                  <FaExclamationTriangle /> {r.risk}
                </p>

                <p>{r.explanation}</p>
              </div>
            ))}
          </>
        )}
      </div>
    </div>
  );
}

// 🎨 Premium Styles
const styles = {
  container: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    padding: 40,
    minHeight: "100vh",
    background: "linear-gradient(135deg, #0f172a, #1e293b, #020617)",
  },

  card: {
    width: "850px",
    background: "rgba(255,255,255,0.05)",
    backdropFilter: "blur(20px)",
    padding: 30,
    borderRadius: 16,
    boxShadow: "0 20px 60px rgba(0,0,0,0.6)",
    border: "1px solid rgba(255,255,255,0.1)",
    color: "white",
  },

  title: {
    textAlign: "center",
    marginBottom: 5,
    color: "#facc15",
    fontSize: "28px",
    fontWeight: "bold",
    textShadow: "0 0 15px rgba(250,204,21,0.8)",
  },

  subtitle: {
    textAlign: "center",
    color: "#94a3b8",
    marginBottom: 25,
    fontSize: "14px",
  },

  uploadBox: {
    display: "flex",
    gap: 10,
    justifyContent: "center",
    marginBottom: 20,
  },

  button: {
    padding: "10px 18px",
    background: "linear-gradient(135deg, #3b82f6, #2563eb)",
    color: "white",
    border: "none",
    borderRadius: 8,
    cursor: "pointer",
    fontWeight: "bold",
    transition: "0.3s",
  },

  text: {
    background: "rgba(255,255,255,0.05)",
    padding: 12,
    borderRadius: 8,
    color: "#e2e8f0",
    lineHeight: "1.6",
  },

  meter: {
    width: "100%",
    height: 18,
    background: "rgba(255,255,255,0.1)",
    borderRadius: 10,
    marginBottom: 10,
    overflow: "hidden",
  },

  meterFill: {
    height: "100%",
    borderRadius: 10,
    transition: "0.5s ease",
  },

  riskCard: {
    background: "rgba(255,255,255,0.05)",
    padding: 15,
    marginTop: 15,
    borderRadius: 12,
    boxShadow: "0 10px 25px rgba(0,0,0,0.4)",
    border: "1px solid rgba(255,255,255,0.08)",
    transition: "0.3s",
  },
};
export default App;