import json

with open('/Users/quocthong248/.gemini/antigravity/scratch/hsk-vocab-app/vocab.json', 'r', encoding='utf-8') as f:
    vocab = json.load(f)

vocab_json_str = json.dumps(vocab, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>HSK Lessons 1–15 Vocabulary Review</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #f8fafc;
      --surface: #ffffff;
      --surface-subtle: #f1f5f9;
      --surface-border: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-subtle: #94a3b8;
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-light: #eef2ff;
      --primary-text: #4338ca;
      --accent: #0ea5e9;
      --success: #10b981;
      --success-light: #ecfdf5;
      --danger: #ef4444;
      --danger-light: #fef2f2;
      --warning: #f59e0b;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.07);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.08), 0 4px 6px -4px rgb(0 0 0 / 0.08);
      --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
      --font-hanzi: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', -apple-system, sans-serif;
      --radius: 12px;
      --radius-sm: 8px;
      --radius-lg: 16px;
      --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    [data-theme="dark"] {
      --bg: #090d16;
      --surface: #131b2e;
      --surface-subtle: #1e293b;
      --surface-border: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-subtle: #64748b;
      --primary: #6366f1;
      --primary-hover: #818cf8;
      --primary-light: rgba(99, 102, 241, 0.18);
      --primary-text: #a5b4fc;
      --accent: #38bdf8;
      --success: #10b981;
      --success-light: rgba(16, 185, 129, 0.18);
      --danger: #f87171;
      --danger-light: rgba(239, 68, 68, 0.18);
      --warning: #fbbf24;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.3);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.35);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.4);
      --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.5);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.5;
      transition: background-color 0.25s ease, color 0.25s ease;
    }

    .container {
      width: 100%;
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 20px;
    }

    /* Header */
    header {
      background: var(--surface);
      border-bottom: 1px solid var(--surface-border);
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
      transition: var(--transition);
    }

    .header-content {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 0;
      gap: 16px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-icon {
      width: 44px;
      height: 44px;
      border-radius: var(--radius-sm);
      background: linear-gradient(135deg, var(--primary), var(--accent));
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-family: var(--font-hanzi);
      font-weight: 700;
      font-size: 24px;
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
      user-select: none;
    }

    .brand-text h1 {
      font-size: 1.25rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text-main);
      line-height: 1.2;
    }

    .brand-text p {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .stat-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--surface-subtle);
      border: 1px solid var(--surface-border);
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 0.825rem;
      font-weight: 600;
      color: var(--text-muted);
    }

    .stat-badge strong {
      color: var(--primary);
      font-weight: 700;
    }

    .header-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--surface-subtle);
      border: 1px solid var(--surface-border);
      color: var(--text-main);
      padding: 7px 14px;
      border-radius: 9999px;
      font-size: 0.825rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
      user-select: none;
    }

    .header-btn:hover {
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary);
    }

    .header-btn.is-hidden {
      background: var(--warning);
      color: #ffffff;
      border-color: var(--warning);
      box-shadow: 0 2px 8px rgba(245, 158, 11, 0.35);
    }

    .theme-toggle-btn {
      background: var(--surface-subtle);
      border: 1px solid var(--surface-border);
      color: var(--text-main);
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
      font-size: 1.15rem;
    }

    .theme-toggle-btn:hover {
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary);
      transform: rotate(15deg);
    }

    /* Toolbar / Filters */
    .toolbar-section {
      padding: 24px 0 16px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .toolbar-top {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      align-items: center;
      justify-content: space-between;
    }

    .search-box {
      position: relative;
      flex: 1 1 320px;
    }

    .search-box svg {
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      width: 18px;
      height: 18px;
      color: var(--text-subtle);
      pointer-events: none;
    }

    .search-input {
      width: 100%;
      height: 44px;
      padding: 0 40px 0 42px;
      border-radius: var(--radius);
      border: 1px solid var(--surface-border);
      background: var(--surface);
      color: var(--text-main);
      font-family: inherit;
      font-size: 0.95rem;
      outline: none;
      transition: var(--transition);
      box-shadow: var(--shadow-sm);
    }

    .search-input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px var(--primary-light);
    }

    .clear-search-btn {
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      color: var(--text-subtle);
      cursor: pointer;
      font-size: 1.2rem;
      display: none;
      padding: 4px;
      line-height: 1;
    }

    .clear-search-btn:hover {
      color: var(--text-main);
    }

    /* Mode Navigation Tabs */
    .mode-nav {
      display: inline-flex;
      background: var(--surface);
      border: 1px solid var(--surface-border);
      padding: 4px;
      border-radius: var(--radius);
      box-shadow: var(--shadow-sm);
    }

    .mode-tab-btn {
      border: none;
      background: transparent;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      font-size: 0.875rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: var(--transition);
    }

    .mode-tab-btn.active {
      background: var(--primary);
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(79, 70, 229, 0.35);
    }

    .mode-tab-btn:not(.active):hover {
      color: var(--text-main);
      background: var(--surface-subtle);
    }

    /* Lesson Filter Pills Bar */
    .lesson-scroll-container {
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      padding: 4px 2px 10px;
      scrollbar-width: thin;
      scrollbar-color: var(--surface-border) transparent;
      -webkit-overflow-scrolling: touch;
    }

    .lesson-scroll-container::-webkit-scrollbar {
      height: 6px;
    }

    .lesson-scroll-container::-webkit-scrollbar-thumb {
      background: var(--surface-border);
      border-radius: 9999px;
    }

    .lesson-pill {
      white-space: nowrap;
      border: 1px solid var(--surface-border);
      background: var(--surface);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 0.825rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
      user-select: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .lesson-pill:hover {
      border-color: var(--primary);
      color: var(--primary);
      background: var(--surface-subtle);
    }

    .lesson-pill.active {
      background: var(--primary-light);
      border-color: var(--primary);
      color: var(--primary-text);
      font-weight: 700;
    }

    .pill-count {
      font-size: 0.75rem;
      background: var(--surface-subtle);
      padding: 1px 6px;
      border-radius: 9999px;
      color: inherit;
      opacity: 0.85;
    }

    /* Views Common Container */
    .view-content {
      padding: 10px 0 40px;
      flex: 1;
    }

    .view-pane {
      display: none;
      animation: fadeIn 0.25s ease forwards;
    }

    .view-pane.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* MODE A: Table View */
    .table-tools-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 16px;
      padding: 12px 16px;
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius);
    }

    .table-tool-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .table-tool-title {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-subtle);
      margin-right: 4px;
    }

    .toggle-chip {
      background: var(--surface-subtle);
      border: 1px solid var(--surface-border);
      color: var(--text-muted);
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition);
      user-select: none;
    }

    .toggle-chip.active {
      background: var(--primary-light);
      border-color: var(--primary);
      color: var(--primary-text);
    }

    .table-card {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
    }

    .table-wrapper {
      width: 100%;
      overflow-x: auto;
    }

    table.vocab-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.925rem;
    }

    table.vocab-table th {
      background: var(--surface-subtle);
      color: var(--text-muted);
      font-weight: 700;
      font-size: 0.775rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 14px 18px;
      border-bottom: 1px solid var(--surface-border);
      white-space: nowrap;
    }

    table.vocab-table td {
      padding: 14px 18px;
      border-bottom: 1px solid var(--surface-border);
      vertical-align: middle;
      color: var(--text-main);
    }

    table.vocab-table tbody tr {
      transition: background-color 0.15s ease;
    }

    table.vocab-table tbody tr:hover {
      background-color: var(--surface-subtle);
    }

    table.vocab-table tr:last-child td {
      border-bottom: none;
    }

    .lesson-badge {
      display: inline-block;
      padding: 3px 8px;
      font-size: 0.75rem;
      font-weight: 700;
      border-radius: 6px;
      background: var(--surface-subtle);
      color: var(--text-muted);
      border: 1px solid var(--surface-border);
      white-space: nowrap;
    }

    .hanzi-cell {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .hanzi-text {
      font-family: var(--font-hanzi);
      font-size: 1.6rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      color: var(--text-main);
      line-height: 1.1;
    }

    .tts-btn {
      background: var(--surface-subtle);
      border: 1px solid var(--surface-border);
      color: var(--text-muted);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
      flex-shrink: 0;
    }

    .tts-btn:hover {
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary);
      transform: scale(1.08);
    }

    .tts-btn:active {
      transform: scale(0.95);
    }

    .pinyin-text {
      color: var(--primary-text);
      font-weight: 600;
      font-size: 0.95rem;
      letter-spacing: 0.02em;
    }

    .meaning-vi {
      font-weight: 500;
      color: var(--text-main);
    }

    .meaning-en {
      color: var(--text-muted);
      font-size: 0.88rem;
    }

    .blur-mask {
      filter: blur(6px);
      user-select: none;
      cursor: pointer;
      transition: filter 0.2s ease;
      background: rgba(148, 163, 184, 0.15);
      border-radius: 4px;
      padding: 2px 6px;
    }

    .blur-mask:hover {
      filter: blur(2px);
    }

    .empty-state {
      text-align: center;
      padding: 60px 20px;
      color: var(--text-muted);
    }

    .empty-state svg {
      width: 48px;
      height: 48px;
      margin-bottom: 12px;
      opacity: 0.4;
    }

    /* MODE B: Interactive Flashcards */
    .flashcard-section {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 24px;
      max-width: 620px;
      margin: 10px auto 30px;
    }

    .flashcard-header-bar {
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: var(--text-muted);
      font-size: 0.9rem;
      font-weight: 600;
    }

    .progress-bar-wrap {
      width: 100%;
      height: 6px;
      background: var(--surface-subtle);
      border-radius: 9999px;
      overflow: hidden;
      border: 1px solid var(--surface-border);
    }

    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--primary), var(--accent));
      width: 0%;
      transition: width 0.3s ease;
    }

    .flashcard-stage {
      width: 100%;
      height: 360px;
      perspective: 1200px;
      cursor: pointer;
      user-select: none;
    }

    .flashcard-inner {
      position: relative;
      width: 100%;
      height: 100%;
      transform-style: preserve-3d;
      transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-xl);
    }

    .flashcard-inner.flipped {
      transform: rotateY(180deg);
    }

    .flashcard-face {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      border-radius: var(--radius-lg);
      border: 1px solid var(--surface-border);
      background: var(--surface);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 32px;
      text-align: center;
    }

    .flashcard-front {
      background: radial-gradient(circle at top right, var(--surface-subtle), var(--surface));
    }

    .flashcard-back {
      transform: rotateY(180deg);
      background: radial-gradient(circle at bottom left, var(--surface-subtle), var(--surface));
      gap: 12px;
    }

    .fc-lesson-chip {
      position: absolute;
      top: 18px;
      left: 20px;
      font-size: 0.78rem;
      font-weight: 700;
      background: var(--surface-subtle);
      border: 1px solid var(--surface-border);
      padding: 4px 10px;
      border-radius: 9999px;
      color: var(--text-muted);
    }

    .fc-hint-chip {
      position: absolute;
      bottom: 18px;
      color: var(--text-subtle);
      font-size: 0.8rem;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .fc-hanzi-large {
      font-family: var(--font-hanzi);
      font-size: 4.8rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.1;
      margin-bottom: 8px;
    }

    .fc-pinyin-back {
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--primary);
      letter-spacing: 0.02em;
      transition: filter 0.2s ease;
    }

    .fc-hanzi-back {
      font-family: var(--font-hanzi);
      font-size: 2.2rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.1;
    }

    .fc-divider {
      width: 60px;
      height: 3px;
      background: var(--surface-border);
      border-radius: 9999px;
      margin: 4px 0;
    }

    .fc-vi-back {
      font-size: 1.2rem;
      font-weight: 600;
      color: var(--text-main);
    }

    .fc-en-back {
      font-size: 1rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .flashcard-controls {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      width: 100%;
      flex-wrap: wrap;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 18px;
      border-radius: var(--radius);
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--surface-border);
      background: var(--surface);
      color: var(--text-main);
      box-shadow: var(--shadow-sm);
      transition: var(--transition);
      user-select: none;
    }

    .btn:hover {
      background: var(--surface-subtle);
      border-color: var(--text-subtle);
    }

    .btn:active {
      transform: scale(0.97);
    }

    .btn-primary {
      background: var(--primary);
      border-color: var(--primary);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    }

    .btn-primary:hover {
      background: var(--primary-hover);
      border-color: var(--primary-hover);
    }

    .btn-icon-only {
      width: 44px;
      height: 44px;
      padding: 0;
      border-radius: 50%;
    }

    /* MODE C: Quiz Mode */
    .quiz-section {
      max-width: 680px;
      margin: 10px auto 40px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .quiz-card,
    .quiz-result-card {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-lg);
      padding: 30px;
      box-shadow: var(--shadow-lg);
    }

    .quiz-top-stats {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-muted);
    }

    .quiz-score-pill {
      background: var(--primary-light);
      color: var(--primary-text);
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 0.85rem;
    }

    .quiz-mode-selector {
      display: flex;
      background: var(--surface-subtle);
      border: 1px solid var(--surface-border);
      padding: 4px;
      border-radius: var(--radius);
      margin-bottom: 24px;
    }

    .quiz-mode-pill {
      flex: 1;
      padding: 10px;
      text-align: center;
      border-radius: var(--radius-sm);
      font-size: 0.875rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      border: none;
      background: transparent;
      transition: var(--transition);
    }

    .quiz-mode-pill.active {
      background: var(--surface);
      color: var(--text-main);
      box-shadow: var(--shadow-sm);
      font-weight: 700;
    }

    .quiz-question-box {
      text-align: center;
      padding: 24px 12px 30px;
      border-bottom: 1px solid var(--surface-border);
      margin-bottom: 24px;
    }

    .quiz-prompt-label {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-subtle);
      margin-bottom: 10px;
    }

    .quiz-prompt-main {
      font-size: 2.8rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.2;
      font-family: var(--font-hanzi);
      display: inline-flex;
      align-items: center;
      gap: 14px;
      justify-content: center;
    }

    .quiz-prompt-sub {
      font-size: 1.1rem;
      color: var(--primary);
      font-weight: 600;
      margin-top: 6px;
      transition: filter 0.2s ease;
    }

    .quiz-options-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }

    @media (min-width: 600px) {
      .quiz-options-grid {
        grid-template-columns: 1fr 1fr;
      }
    }

    .quiz-option-btn {
      background: var(--surface-subtle);
      border: 1.5px solid var(--surface-border);
      border-radius: var(--radius);
      padding: 16px 20px;
      font-size: 1rem;
      font-weight: 600;
      color: var(--text-main);
      cursor: pointer;
      text-align: left;
      transition: var(--transition);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      line-height: 1.35;
    }

    .quiz-option-btn:not(:disabled):hover {
      background: var(--surface);
      border-color: var(--primary);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }

    .quiz-option-btn:disabled {
      cursor: default;
    }

    .quiz-option-btn.opt-correct {
      background: var(--success-light) !important;
      border-color: var(--success) !important;
      color: #065f46 !important;
      font-weight: 700;
    }

    [data-theme="dark"] .quiz-option-btn.opt-correct {
      color: #6ee7b7 !important;
    }

    .quiz-option-btn.opt-wrong {
      background: var(--danger-light) !important;
      border-color: var(--danger) !important;
      color: #991b1b !important;
    }

    [data-theme="dark"] .quiz-option-btn.opt-wrong {
      color: #fca5a5 !important;
    }

    .quiz-feedback-bar {
      margin-top: 20px;
      padding: 14px 18px;
      border-radius: var(--radius);
      display: none;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      animation: fadeIn 0.2s ease forwards;
    }

    .quiz-feedback-bar.correct {
      background: var(--success-light);
      border: 1px solid var(--success);
      color: #065f46;
    }

    [data-theme="dark"] .quiz-feedback-bar.correct {
      color: #6ee7b7;
    }

    .quiz-feedback-bar.wrong {
      background: var(--danger-light);
      border: 1px solid var(--danger);
      color: #991b1b;
    }

    [data-theme="dark"] .quiz-feedback-bar.wrong {
      color: #fca5a5;
    }

    .quiz-result-score-circle {
      width: 120px;
      height: 120px;
      border-radius: 50%;
      background: var(--primary-light);
      border: 4px solid var(--primary);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin: 20px auto;
      color: var(--primary);
      font-weight: 800;
      font-size: 2.2rem;
      line-height: 1;
    }

    .quiz-result-score-circle span {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-top: 4px;
    }

    /* Footer */
    footer {
      margin-top: auto;
      border-top: 1px solid var(--surface-border);
      background: var(--surface);
      padding: 20px 0;
      font-size: 0.85rem;
      color: var(--text-muted);
      text-align: center;
    }

    .kbd-key {
      display: inline-block;
      padding: 2px 6px;
      font-size: 0.72rem;
      font-weight: 700;
      border-radius: 4px;
      background: var(--surface-subtle);
      border: 1px solid var(--surface-border);
      color: var(--text-subtle);
      box-shadow: 0 1px 1px rgba(0,0,0,0.1);
      vertical-align: middle;
    }

    @media (max-width: 768px) {
      .header-content {
        flex-direction: column;
        align-items: flex-start;
      }
      .header-actions {
        width: 100%;
        justify-content: flex-start;
      }
      .toolbar-top {
        flex-direction: column;
        align-items: stretch;
      }
      .mode-nav {
        width: 100%;
        display: flex;
      }
      .mode-tab-btn {
        flex: 1;
        justify-content: center;
        padding: 8px 10px;
        font-size: 0.8rem;
      }
      .flashcard-stage {
        height: 320px;
      }
      .fc-hanzi-large {
        font-size: 3.8rem;
      }
    }
  </style>
</head>
<body>

  <!-- App Header -->
  <header>
    <div class="container header-content">
      <div class="brand">
        <div class="brand-icon">汉</div>
        <div class="brand-text">
          <h1>HSK Lessons 1–15 Vocabulary Review</h1>
          <p>Complete curriculum • 322 items • Audio TTS &amp; Quizzes</p>
        </div>
      </div>
      <div class="header-actions">
        <div class="stat-badge">
          Showing: <strong id="stat-showing">322</strong> / <span id="stat-total">322</span> words
        </div>
        <!-- Global Hide/Show Pinyin Button -->
        <button class="header-btn" id="global-toggle-pinyin-btn" title="Toggle Pinyin visibility for active study mode" aria-label="Toggle Pinyin">
          <span id="global-pinyin-icon">👁️</span>
          <span id="global-pinyin-text">Hide Pinyin</span>
        </button>
        <button class="theme-toggle-btn" id="theme-toggle-btn" title="Toggle Dark/Light Mode" aria-label="Toggle theme">
          <span id="theme-icon">🌙</span>
        </button>
      </div>
    </div>
  </header>

  <main class="container">
    <!-- Toolbar Section -->
    <section class="toolbar-section">
      <div class="toolbar-top">
        <div class="search-box">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input 
            type="text" 
            id="search-input" 
            class="search-input" 
            placeholder="Search characters, pinyin, Vietnamese or English (e.g. 咖啡, ni hao, bạn, water)..." 
            autocomplete="off"
          />
          <button id="clear-search-btn" class="clear-search-btn" title="Clear search">&times;</button>
        </div>

        <nav class="mode-nav" aria-label="Study modes">
          <button class="mode-tab-btn active" data-mode="table">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3h18v18H3z"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v18"/></svg>
            Table View
          </button>
          <button class="mode-tab-btn" data-mode="flashcards">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>
            Flashcards
          </button>
          <button class="mode-tab-btn" data-mode="quiz">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
            Quiz Mode
          </button>
        </nav>
      </div>

      <!-- Lesson Pills Filter -->
      <div class="lesson-scroll-container" id="lesson-pills-bar">
        <!-- Injected via JavaScript -->
      </div>
    </section>

    <!-- Views Container -->
    <div class="view-content">

      <!-- MODE A: Table View -->
      <section id="view-table" class="view-pane active">
        <div class="table-tools-bar">
          <div class="table-tool-group">
            <span class="table-tool-title">Self-Test Blur:</span>
            <button class="toggle-chip" id="toggle-hide-pinyin">
              <span id="table-pinyin-chip-icon">👁️</span> Hide Pinyin
            </button>
            <button class="toggle-chip" id="toggle-hide-vi">
              <span>👁️</span> Hide Vietnamese
            </button>
            <button class="toggle-chip" id="toggle-hide-en">
              <span>👁️</span> Hide English
            </button>
          </div>
          <div class="table-tool-group">
            <button class="btn" id="btn-shuffle-table" style="padding: 5px 12px; font-size: 0.8rem;">
              <span>🔀</span> Shuffle List
            </button>
            <button class="btn" id="btn-reset-table-sort" style="padding: 5px 12px; font-size: 0.8rem;">
              <span>🔄</span> Original Order
            </button>
          </div>
        </div>

        <div class="table-card">
          <div class="table-wrapper">
            <table class="vocab-table">
              <thead>
                <tr>
                  <th style="width: 70px;">Lesson</th>
                  <th style="width: 60px;">No.</th>
                  <th style="min-width: 170px;">Word / Characters</th>
                  <th style="min-width: 160px;" class="col-pinyin">Pinyin</th>
                  <th style="min-width: 220px;" class="col-vi">Vietnamese Meaning</th>
                  <th style="min-width: 220px;" class="col-en">English Meaning</th>
                </tr>
              </thead>
              <tbody id="vocab-table-body">
                <!-- Rows injected dynamically -->
              </tbody>
            </table>
          </div>
          <div id="table-empty-msg" class="empty-state" style="display: none;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <p>No vocabulary words match your current filters or search query.</p>
          </div>
        </div>
      </section>

      <!-- MODE B: Interactive Flashcards -->
      <section id="view-flashcards" class="view-pane">
        <div class="flashcard-section">
          <div class="flashcard-header-bar">
            <span id="fc-counter-label">Card 1 of 322</span>
            <span>Shortcut: <span class="kbd-key">Space</span> flip, <span class="kbd-key">&larr;</span> / <span class="kbd-key">&rarr;</span> prev/next</span>
          </div>

          <div class="progress-bar-wrap">
            <div id="fc-progress-fill" class="progress-bar-fill"></div>
          </div>

          <!-- Flip Card Container -->
          <div class="flashcard-stage" id="flashcard-stage" title="Click or press Spacebar to flip card">
            <div class="flashcard-inner" id="flashcard-inner">
              <!-- Front -->
              <div class="flashcard-face flashcard-front">
                <span class="fc-lesson-chip" id="fc-front-lesson">Lesson 1</span>
                <div class="fc-hanzi-large" id="fc-front-hanzi">你好</div>
                <div class="fc-hint-chip">
                  <span>💡 Click card or tap Space to flip</span>
                </div>
              </div>
              <!-- Back -->
              <div class="flashcard-face flashcard-back">
                <span class="fc-lesson-chip" id="fc-back-lesson">Lesson 1</span>
                <div class="fc-hanzi-back" id="fc-back-hanzi">你好</div>
                <div class="fc-pinyin-back" id="fc-back-pinyin">nǐ hǎo</div>
                <div class="fc-divider"></div>
                <div class="fc-vi-back" id="fc-back-vi">xin chào</div>
                <div class="fc-en-back" id="fc-back-en">hello</div>
              </div>
            </div>
          </div>

          <!-- Controls -->
          <div class="flashcard-controls">
            <button class="btn btn-icon-only" id="fc-prev-btn" title="Previous card (Left Arrow)">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
            </button>
            <button class="btn" id="fc-tts-btn" title="Pronounce (TTS)">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
              Pronounce
            </button>
            <button class="btn btn-primary" id="fc-flip-btn" title="Flip card (Spacebar)">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 2v6h-6"/><path d="M3 12a9 9 0 0 1 15-6.7L21 8"/><path d="M3 22v-6h6"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16"/></svg>
              Flip Card
            </button>
            <button class="btn" id="fc-toggle-pinyin-btn" title="Toggle Pinyin on back of flashcard">
              <span id="fc-pinyin-btn-icon">👁️</span>
              <span id="fc-pinyin-btn-text">Hide Pinyin</span>
            </button>
            <button class="btn" id="fc-shuffle-btn" title="Shuffle deck">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/><line x1="4" y1="4" x2="9" y2="9"/></svg>
              Shuffle
            </button>
            <button class="btn btn-icon-only" id="fc-next-btn" title="Next card (Right Arrow)">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
            </button>
          </div>
        </div>
      </section>

      <!-- MODE C: Quiz Mode -->
      <section id="view-quiz" class="view-pane">
        <div class="quiz-section">
          <!-- Quiz Container Card -->
          <div class="quiz-card" id="quiz-active-box">
            <div class="quiz-top-stats">
              <span id="quiz-question-counter">Question 1 / 10</span>
              <span class="quiz-score-pill" id="quiz-score-indicator">Score: 0 / 0</span>
            </div>

            <!-- Quiz Type Selector -->
            <div class="quiz-mode-selector">
              <button class="quiz-mode-pill active" id="quiz-type-hanzi2meaning" data-type="h2m">
                Hanzi &rarr; Meanings (EN/VI)
              </button>
              <button class="quiz-mode-pill" id="quiz-type-meaning2hanzi" data-type="m2h">
                Meaning &rarr; Hanzi Characters
              </button>
            </div>

            <!-- Question prompt area -->
            <div class="quiz-question-box">
              <div class="quiz-prompt-label" id="quiz-prompt-label">Select the correct translation:</div>
              <div class="quiz-prompt-main">
                <span id="quiz-prompt-text">你好</span>
                <button class="tts-btn" id="quiz-tts-btn" title="Pronounce character" style="width: 38px; height: 38px;">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                </button>
              </div>
              <div class="quiz-prompt-sub" id="quiz-prompt-sub">nǐ hǎo</div>
            </div>

            <!-- Options Grid -->
            <div class="quiz-options-grid" id="quiz-options-container">
              <!-- 4 buttons dynamically injected -->
            </div>

            <!-- Feedback & Next Button -->
            <div class="quiz-feedback-bar" id="quiz-feedback-bar">
              <div id="quiz-feedback-msg" style="font-weight: 700; font-size: 1rem;"></div>
              <button class="btn btn-primary" id="quiz-next-btn">Next Question &rarr;</button>
            </div>
          </div>

          <!-- Final Summary Score Screen -->
          <div class="quiz-result-card" id="quiz-summary-box" style="display: none; text-align: center;">
            <h2 style="font-size: 1.6rem; font-weight: 800; margin-bottom: 6px;">Quiz Completed! 🎉</h2>
            <p style="color: var(--text-muted); font-size: 0.95rem;">Great effort reviewing your HSK vocabulary!</p>
            
            <div class="quiz-result-score-circle">
              <div id="summary-percentage">100%</div>
              <span id="summary-score-fraction">10 / 10</span>
            </div>

            <p id="summary-feedback-comment" style="font-weight: 600; margin-bottom: 24px; color: var(--text-main);"></p>

            <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
              <button class="btn btn-primary" id="quiz-restart-btn">
                <span>🔄</span> Retake Quiz
              </button>
              <button class="btn" id="quiz-back-table-btn">
                <span>📋</span> Review in Table View
              </button>
            </div>
          </div>
        </div>
      </section>

    </div>
  </main>

  <!-- Footer -->
  <footer>
    <div class="container">
      <p>HSK Lessons 1–15 Comprehensive Study System • Standard Chinese Pronunciation (zh-CN) • Built with Vanilla Web Tech</p>
    </div>
  </footer>

  <!-- SCRIPT -->
  <script>
    /* Complete Vocabulary Database */
    const VOCAB_DATA = __VOCAB_PLACEHOLDER__;

    /* State Management */
    const state = {
      selectedLesson: 'all',
      searchQuery: '',
      activeMode: 'table',
      theme: localStorage.getItem('hsk_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'),
      
      // Global Pinyin toggle setting
      hidePinyin: false,
      hideVi: false,
      hideEn: false,

      // Table view options
      tableItems: [...VOCAB_DATA],

      // Flashcards
      fcDeck: [...VOCAB_DATA],
      fcIndex: 0,
      fcFlipped: false,

      // Quiz
      quizType: 'h2m',
      quizPool: [...VOCAB_DATA],
      quizIndex: 0,
      quizTotal: 10,
      quizScore: 0,
      quizAnswered: false,
      currentQuizQuestion: null
    };

    /* Speech Synthesis Helper */
    function speakChinese(text) {
      if (!('speechSynthesis' in window)) {
        alert('Web Speech API is not supported in this browser.');
        return;
      }
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'zh-CN';
      utterance.rate = 0.85;

      const voices = window.speechSynthesis.getVoices();
      const zhVoice = voices.find(v => v.lang.startsWith('zh') || v.lang === 'cmn-Hans-CN' || v.lang === 'zh-CN');
      if (zhVoice) {
        utterance.voice = zhVoice;
      }
      window.speechSynthesis.speak(utterance);
    }

    if ('speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
      };
    }

    /* Helper: Filter vocabulary by lesson and search query */
    function getFilteredVocab() {
      return VOCAB_DATA.filter(item => {
        const matchesLesson = (state.selectedLesson === 'all') || (item.lesson === parseInt(state.selectedLesson));
        if (!matchesLesson) return false;

        if (!state.searchQuery) return true;
        const q = state.searchQuery.toLowerCase().trim();
        return item.chinese.toLowerCase().includes(q) ||
               item.pinyin.toLowerCase().includes(q) ||
               item.vi.toLowerCase().includes(q) ||
               item.en.toLowerCase().includes(q);
      });
    }

    /* Theme Toggle */
    function applyTheme(theme) {
      document.documentElement.setAttribute('data-theme', theme);
      state.theme = theme;
      localStorage.setItem('hsk_theme', theme);
      const icon = document.getElementById('theme-icon');
      if (icon) {
        icon.textContent = theme === 'dark' ? '☀️' : '🌙';
      }
    }

    /* Pinyin Visibility Synchronizer */
    function togglePinyinVisibility() {
      state.hidePinyin = !state.hidePinyin;
      updatePinyinUI();
    }

    function updatePinyinUI() {
      const isHidden = state.hidePinyin;

      // 1. Header Global Button
      const globalBtn = document.getElementById('global-toggle-pinyin-btn');
      const globalIcon = document.getElementById('global-pinyin-icon');
      const globalText = document.getElementById('global-pinyin-text');
      if (globalBtn) {
        globalBtn.classList.toggle('is-hidden', isHidden);
        globalIcon.textContent = isHidden ? '🙈' : '👁️';
        globalText.textContent = isHidden ? 'Show Pinyin' : 'Hide Pinyin';
      }

      // 2. Table Self-Test Chip
      const tableChip = document.getElementById('toggle-hide-pinyin');
      const tableChipIcon = document.getElementById('table-pinyin-chip-icon');
      if (tableChip) {
        tableChip.classList.toggle('active', isHidden);
        if (tableChipIcon) tableChipIcon.textContent = isHidden ? '🙈' : '👁️';
      }

      // 3. Flashcard Control Button
      const fcBtn = document.getElementById('fc-toggle-pinyin-btn');
      const fcIcon = document.getElementById('fc-pinyin-btn-icon');
      const fcText = document.getElementById('fc-pinyin-btn-text');
      if (fcBtn) {
        fcBtn.classList.toggle('btn-primary', isHidden);
        if (fcIcon) fcIcon.textContent = isHidden ? '🙈' : '👁️';
        if (fcText) fcText.textContent = isHidden ? 'Show Pinyin' : 'Hide Pinyin';
      }

      // 4. Update Table Rows
      renderTable();

      // 5. Update Flashcard Back
      const fcPinyinBack = document.getElementById('fc-back-pinyin');
      if (fcPinyinBack) {
        if (isHidden) {
          fcPinyinBack.classList.add('blur-mask');
          fcPinyinBack.title = 'Click to reveal Pinyin';
        } else {
          fcPinyinBack.classList.remove('blur-mask');
          fcPinyinBack.title = '';
        }
      }

      // 6. Update Quiz Prompt Subtitle
      const quizPromptSub = document.getElementById('quiz-prompt-sub');
      if (quizPromptSub && state.quizType === 'h2m') {
        if (isHidden) {
          quizPromptSub.classList.add('blur-mask');
          quizPromptSub.title = 'Click to reveal Pinyin';
        } else {
          quizPromptSub.classList.remove('blur-mask');
          quizPromptSub.title = '';
        }
      }
    }

    /* Render Lesson Filter Pills */
    function renderLessonPills() {
      const container = document.getElementById('lesson-pills-bar');
      container.innerHTML = '';

      const allPill = document.createElement('button');
      allPill.className = `lesson-pill ${state.selectedLesson === 'all' ? 'active' : ''}`;
      allPill.innerHTML = `All Lessons <span class="pill-count">${VOCAB_DATA.length}</span>`;
      allPill.addEventListener('click', () => selectLesson('all'));
      container.appendChild(allPill);

      for (let i = 1; i <= 15; i++) {
        const count = VOCAB_DATA.filter(v => v.lesson === i).length;
        const pill = document.createElement('button');
        pill.className = `lesson-pill ${state.selectedLesson === String(i) ? 'active' : ''}`;
        pill.innerHTML = `Lesson ${i} <span class="pill-count">${count}</span>`;
        pill.addEventListener('click', () => selectLesson(String(i)));
        container.appendChild(pill);
      }
    }

    function selectLesson(lesson) {
      state.selectedLesson = lesson;
      renderLessonPills();
      updateFilteredViews();
    }

    /* Update All Active Views when filters change */
    function updateFilteredViews() {
      const filtered = getFilteredVocab();
      document.getElementById('stat-showing').textContent = filtered.length;
      document.getElementById('stat-total').textContent = VOCAB_DATA.length;

      // Table view update
      state.tableItems = [...filtered];
      renderTable();

      // Flashcards update
      state.fcDeck = filtered.length > 0 ? [...filtered] : [...VOCAB_DATA];
      state.fcIndex = 0;
      state.fcFlipped = false;
      renderFlashcard();

      // Quiz reset with current filter
      initQuiz();
    }

    /* MODE A: Table View Logic */
    function renderTable() {
      const tbody = document.getElementById('vocab-table-body');
      const emptyMsg = document.getElementById('table-empty-msg');
      tbody.innerHTML = '';

      if (state.tableItems.length === 0) {
        emptyMsg.style.display = 'block';
        return;
      }
      emptyMsg.style.display = 'none';

      const frag = document.createDocumentFragment();
      state.tableItems.forEach(item => {
        const tr = document.createElement('tr');

        // Lesson
        const tdLesson = document.createElement('td');
        tdLesson.innerHTML = `<span class="lesson-badge">L${item.lesson}</span>`;

        // No
        const tdNo = document.createElement('td');
        tdNo.style.color = 'var(--text-subtle)';
        tdNo.style.fontWeight = '600';
        tdNo.textContent = '#' + item.no;

        // Chinese + Audio
        const tdHanzi = document.createElement('td');
        tdHanzi.innerHTML = `
          <div class="hanzi-cell">
            <span class="hanzi-text">${item.chinese}</span>
            <button class="tts-btn" title="Pronounce ${item.chinese}">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        `;
        tdHanzi.querySelector('.tts-btn').addEventListener('click', (e) => {
          e.stopPropagation();
          speakChinese(item.chinese);
        });

        // Pinyin
        const tdPinyin = document.createElement('td');
        tdPinyin.className = `pinyin-text col-pinyin ${state.hidePinyin ? 'blur-mask' : ''}`;
        tdPinyin.textContent = item.pinyin;
        tdPinyin.title = state.hidePinyin ? 'Click to reveal' : '';
        tdPinyin.addEventListener('click', () => {
          if (tdPinyin.classList.contains('blur-mask')) {
            tdPinyin.classList.toggle('blur-mask');
          }
        });

        // Vietnamese
        const tdVi = document.createElement('td');
        tdVi.className = `meaning-vi col-vi ${state.hideVi ? 'blur-mask' : ''}`;
        tdVi.textContent = item.vi;
        tdVi.title = state.hideVi ? 'Click to reveal' : '';
        tdVi.addEventListener('click', () => {
          if (tdVi.classList.contains('blur-mask')) {
            tdVi.classList.toggle('blur-mask');
          }
        });

        // English
        const tdEn = document.createElement('td');
        tdEn.className = `meaning-en col-en ${state.hideEn ? 'blur-mask' : ''}`;
        tdEn.textContent = item.en;
        tdEn.title = state.hideEn ? 'Click to reveal' : '';
        tdEn.addEventListener('click', () => {
          if (tdEn.classList.contains('blur-mask')) {
            tdEn.classList.toggle('blur-mask');
          }
        });

        tr.appendChild(tdLesson);
        tr.appendChild(tdNo);
        tr.appendChild(tdHanzi);
        tr.appendChild(tdPinyin);
        tr.appendChild(tdVi);
        tr.appendChild(tdEn);

        frag.appendChild(tr);
      });

      tbody.appendChild(frag);
    }

    /* MODE B: Interactive Flashcards Logic */
    function renderFlashcard() {
      const inner = document.getElementById('flashcard-inner');
      if (state.fcDeck.length === 0) return;

      if (state.fcFlipped) {
        inner.classList.add('flipped');
      } else {
        inner.classList.remove('flipped');
      }

      const item = state.fcDeck[state.fcIndex];
      const total = state.fcDeck.length;

      document.getElementById('fc-counter-label').textContent = `Card ${state.fcIndex + 1} of ${total}`;
      const pct = ((state.fcIndex + 1) / total) * 100;
      document.getElementById('fc-progress-fill').style.width = `${pct}%`;

      document.getElementById('fc-front-lesson').textContent = `Lesson ${item.lesson} (#${item.no})`;
      document.getElementById('fc-front-hanzi').textContent = item.chinese;

      document.getElementById('fc-back-lesson').textContent = `Lesson ${item.lesson} (#${item.no})`;
      document.getElementById('fc-back-hanzi').textContent = item.chinese;
      
      const fcPinyinBack = document.getElementById('fc-back-pinyin');
      fcPinyinBack.textContent = item.pinyin;
      if (state.hidePinyin) {
        fcPinyinBack.classList.add('blur-mask');
        fcPinyinBack.title = 'Click to reveal';
      } else {
        fcPinyinBack.classList.remove('blur-mask');
        fcPinyinBack.title = '';
      }

      document.getElementById('fc-back-vi').textContent = item.vi;
      document.getElementById('fc-back-en').textContent = item.en;
    }

    function flipFlashcard() {
      state.fcFlipped = !state.fcFlipped;
      const inner = document.getElementById('flashcard-inner');
      if (state.fcFlipped) {
        inner.classList.add('flipped');
      } else {
        inner.classList.remove('flipped');
      }
    }

    function nextFlashcard() {
      if (state.fcDeck.length === 0) return;
      state.fcFlipped = false;
      state.fcIndex = (state.fcIndex + 1) % state.fcDeck.length;
      renderFlashcard();
    }

    function prevFlashcard() {
      if (state.fcDeck.length === 0) return;
      state.fcFlipped = false;
      state.fcIndex = (state.fcIndex - 1 + state.fcDeck.length) % state.fcDeck.length;
      renderFlashcard();
    }

    function shuffleFlashcards() {
      for (let i = state.fcDeck.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [state.fcDeck[i], state.fcDeck[j]] = [state.fcDeck[j], state.fcDeck[i]];
      }
      state.fcIndex = 0;
      state.fcFlipped = false;
      renderFlashcard();
    }

    /* MODE C: Quiz Mode Logic */
    function initQuiz() {
      const filtered = getFilteredVocab();
      state.quizPool = filtered.length >= 4 ? [...filtered] : [...VOCAB_DATA];
      
      for (let i = state.quizPool.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [state.quizPool[i], state.quizPool[j]] = [state.quizPool[j], state.quizPool[i]];
      }

      state.quizTotal = Math.min(10, state.quizPool.length);
      state.quizIndex = 0;
      state.quizScore = 0;
      state.quizAnswered = false;

      document.getElementById('quiz-active-box').style.display = 'block';
      document.getElementById('quiz-summary-box').style.display = 'none';

      loadQuizQuestion();
    }

    function loadQuizQuestion() {
      state.quizAnswered = false;
      document.getElementById('quiz-feedback-bar').style.display = 'none';
      document.getElementById('quiz-question-counter').textContent = `Question ${state.quizIndex + 1} of ${state.quizTotal}`;
      document.getElementById('quiz-score-indicator').textContent = `Score: ${state.quizScore} / ${state.quizIndex}`;

      const currentWord = state.quizPool[state.quizIndex];
      state.currentQuizQuestion = currentWord;

      const distractors = [];
      const usedIndices = new Set();
      while (distractors.length < 3) {
        const randIdx = Math.floor(Math.random() * VOCAB_DATA.length);
        const cand = VOCAB_DATA[randIdx];
        if (cand.chinese !== currentWord.chinese && !usedIndices.has(randIdx)) {
          distractors.push(cand);
          usedIndices.add(randIdx);
        }
      }

      const choices = [currentWord, ...distractors];
      for (let i = choices.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [choices[i], choices[j]] = [choices[j], choices[i]];
      }

      const promptLabel = document.getElementById('quiz-prompt-label');
      const promptText = document.getElementById('quiz-prompt-text');
      const promptSub = document.getElementById('quiz-prompt-sub');
      const ttsBtn = document.getElementById('quiz-tts-btn');

      if (state.quizType === 'h2m') {
        promptLabel.textContent = 'Identify the meaning of this word:';
        promptText.textContent = currentWord.chinese;
        promptSub.textContent = currentWord.pinyin;
        if (state.hidePinyin) {
          promptSub.classList.add('blur-mask');
          promptSub.title = 'Click to reveal';
        } else {
          promptSub.classList.remove('blur-mask');
          promptSub.title = '';
        }
        ttsBtn.style.display = 'inline-flex';
        ttsBtn.onclick = () => speakChinese(currentWord.chinese);
      } else {
        promptLabel.textContent = 'Identify the Chinese character for:';
        promptText.textContent = currentWord.vi;
        promptSub.textContent = `En: ${currentWord.en}`;
        promptSub.classList.remove('blur-mask');
        promptSub.title = '';
        ttsBtn.style.display = 'none';
      }

      const container = document.getElementById('quiz-options-container');
      container.innerHTML = '';

      choices.forEach((choice, idx) => {
        const btn = document.createElement('button');
        btn.className = 'quiz-option-btn';

        if (state.quizType === 'h2m') {
          btn.innerHTML = `
            <div>
              <div style="font-size: 1.05rem; font-weight: 700;">${choice.vi}</div>
              <div style="font-size: 0.85rem; color: var(--text-muted); font-weight: 500;">${choice.en}</div>
            </div>
            <span style="font-size: 0.8rem; font-weight: 700; opacity: 0.6;">[${String.fromCharCode(65 + idx)}]</span>
          `;
        } else {
          btn.innerHTML = `
            <div>
              <div style="font-family: var(--font-hanzi); font-size: 1.6rem; font-weight: 700;">${choice.chinese}</div>
              <div style="font-size: 0.9rem; color: var(--primary); font-weight: 600;" class="${state.hidePinyin ? 'blur-mask' : ''}">${choice.pinyin}</div>
            </div>
            <span style="font-size: 0.8rem; font-weight: 700; opacity: 0.6;">[${String.fromCharCode(65 + idx)}]</span>
          `;
        }

        btn.addEventListener('click', () => handleQuizAnswer(choice, btn, choices));
        container.appendChild(btn);
      });
    }

    function handleQuizAnswer(selectedChoice, selectedBtn, allChoices) {
      if (state.quizAnswered) return;
      state.quizAnswered = true;

      const isCorrect = (selectedChoice.chinese === state.currentQuizQuestion.chinese);
      if (isCorrect) {
        state.quizScore++;
      }
      document.getElementById('quiz-score-indicator').textContent = `Score: ${state.quizScore} / ${state.quizIndex + 1}`;

      const buttons = document.querySelectorAll('.quiz-option-btn');
      buttons.forEach((btn, idx) => {
        btn.disabled = true;
        const choice = allChoices[idx];
        if (choice.chinese === state.currentQuizQuestion.chinese) {
          btn.classList.add('opt-correct');
        } else if (btn === selectedBtn && !isCorrect) {
          btn.classList.add('opt-wrong');
        }
      });

      const feedbackBar = document.getElementById('quiz-feedback-bar');
      const feedbackMsg = document.getElementById('quiz-feedback-msg');
      feedbackBar.style.display = 'flex';

      if (isCorrect) {
        feedbackBar.className = 'quiz-feedback-bar correct';
        feedbackMsg.innerHTML = `✨ <strong>Correct!</strong> Well done!`;
      } else {
        feedbackBar.className = 'quiz-feedback-bar wrong';
        feedbackMsg.innerHTML = `❌ <strong>Incorrect!</strong> Correct answer: <strong>${state.currentQuizQuestion.chinese}</strong> (${state.currentQuizQuestion.pinyin}) = ${state.currentQuizQuestion.vi}`;
      }

      speakChinese(state.currentQuizQuestion.chinese);

      const nextBtn = document.getElementById('quiz-next-btn');
      if (state.quizIndex + 1 >= state.quizTotal) {
        nextBtn.textContent = 'View Results 🎉';
      } else {
        nextBtn.innerHTML = 'Next Question &rarr;';
      }
    }

    function nextQuizStep() {
      state.quizIndex++;
      if (state.quizIndex >= state.quizTotal) {
        showQuizSummary();
      } else {
        loadQuizQuestion();
      }
    }

    function showQuizSummary() {
      document.getElementById('quiz-active-box').style.display = 'none';
      const summaryBox = document.getElementById('quiz-summary-box');
      summaryBox.style.display = 'block';

      const pct = Math.round((state.quizScore / state.quizTotal) * 100);
      document.getElementById('summary-percentage').textContent = `${pct}%`;
      document.getElementById('summary-score-fraction').textContent = `${state.quizScore} / ${state.quizTotal} correct`;

      const commentEl = document.getElementById('summary-feedback-comment');
      if (pct === 100) {
        commentEl.textContent = '🏆 Perfect score! You have mastered these vocabulary words!';
      } else if (pct >= 80) {
        commentEl.textContent = '🌟 Excellent job! Almost a flawless review!';
      } else if (pct >= 60) {
        commentEl.textContent = '👍 Good effort! Review the flashcards to strengthen weak spots.';
      } else {
        commentEl.textContent = '💪 Keep practicing! Spend some time in the Table & Flashcards view.';
      }
    }

    /* Setup Event Listeners */
    function setupEventListeners() {
      // Global Pinyin toggle in Header
      document.getElementById('global-toggle-pinyin-btn').addEventListener('click', togglePinyinVisibility);

      // Flashcards Pinyin toggle
      document.getElementById('fc-toggle-pinyin-btn').addEventListener('click', togglePinyinVisibility);

      // Click to toggle blurred pinyin on flashcard back
      document.getElementById('fc-back-pinyin').addEventListener('click', (e) => {
        e.stopPropagation();
        const el = document.getElementById('fc-back-pinyin');
        if (el.classList.contains('blur-mask')) {
          el.classList.toggle('blur-mask');
        }
      });

      // Click to toggle blurred pinyin in Quiz prompt
      document.getElementById('quiz-prompt-sub').addEventListener('click', () => {
        const el = document.getElementById('quiz-prompt-sub');
        if (el.classList.contains('blur-mask')) {
          el.classList.toggle('blur-mask');
        }
      });

      // Theme Toggle
      document.getElementById('theme-toggle-btn').addEventListener('click', () => {
        const nextTheme = state.theme === 'dark' ? 'light' : 'dark';
        applyTheme(nextTheme);
      });

      // Search input
      const searchInput = document.getElementById('search-input');
      const clearBtn = document.getElementById('clear-search-btn');

      searchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value;
        clearBtn.style.display = state.searchQuery ? 'block' : 'none';
        updateFilteredViews();
      });

      clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        state.searchQuery = '';
        clearBtn.style.display = 'none';
        searchInput.focus();
        updateFilteredViews();
      });

      // Mode Navigation
      const modeButtons = document.querySelectorAll('.mode-tab-btn');
      modeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
          const mode = btn.dataset.mode;
          state.activeMode = mode;
          modeButtons.forEach(b => b.classList.toggle('active', b === btn));

          document.querySelectorAll('.view-pane').forEach(p => p.classList.remove('active'));
          const targetView = document.getElementById(`view-${mode}`);
          if (targetView) targetView.classList.add('active');

          if (mode === 'flashcards') {
            renderFlashcard();
          } else if (mode === 'quiz' && state.quizPool.length === 0) {
            initQuiz();
          }
        });
      });

      // Table View Controls
      const btnHidePinyin = document.getElementById('toggle-hide-pinyin');
      btnHidePinyin.addEventListener('click', () => {
        togglePinyinVisibility();
      });

      const btnHideVi = document.getElementById('toggle-hide-vi');
      btnHideVi.addEventListener('click', () => {
        state.hideVi = !state.hideVi;
        btnHideVi.classList.toggle('active', state.hideVi);
        renderTable();
      });

      const btnHideEn = document.getElementById('toggle-hide-en');
      btnHideEn.addEventListener('click', () => {
        state.hideEn = !state.hideEn;
        btnHideEn.classList.toggle('active', state.hideEn);
        renderTable();
      });

      document.getElementById('btn-shuffle-table').addEventListener('click', () => {
        for (let i = state.tableItems.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [state.tableItems[i], state.tableItems[j]] = [state.tableItems[j], state.tableItems[i]];
        }
        renderTable();
      });

      document.getElementById('btn-reset-table-sort').addEventListener('click', () => {
        state.tableItems = getFilteredVocab();
        renderTable();
      });

      // Flashcards Controls
      document.getElementById('flashcard-stage').addEventListener('click', flipFlashcard);
      document.getElementById('fc-flip-btn').addEventListener('click', flipFlashcard);
      document.getElementById('fc-next-btn').addEventListener('click', nextFlashcard);
      document.getElementById('fc-prev-btn').addEventListener('click', prevFlashcard);
      document.getElementById('fc-shuffle-btn').addEventListener('click', shuffleFlashcards);
      document.getElementById('fc-tts-btn').addEventListener('click', () => {
        const item = state.fcDeck[state.fcIndex];
        if (item) speakChinese(item.chinese);
      });

      // Quiz Mode Controls
      document.getElementById('quiz-type-hanzi2meaning').addEventListener('click', (e) => {
        state.quizType = 'h2m';
        document.getElementById('quiz-type-hanzi2meaning').classList.add('active');
        document.getElementById('quiz-type-meaning2hanzi').classList.remove('active');
        initQuiz();
      });

      document.getElementById('quiz-type-meaning2hanzi').addEventListener('click', (e) => {
        state.quizType = 'm2h';
        document.getElementById('quiz-type-meaning2hanzi').classList.add('active');
        document.getElementById('quiz-type-hanzi2meaning').classList.remove('active');
        initQuiz();
      });

      document.getElementById('quiz-next-btn').addEventListener('click', nextQuizStep);
      document.getElementById('quiz-restart-btn').addEventListener('click', initQuiz);
      document.getElementById('quiz-back-table-btn').addEventListener('click', () => {
        document.querySelector('.mode-tab-btn[data-mode="table"]').click();
      });

      // Keyboard shortcuts
      window.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

        // Press 'P' to toggle pinyin anytime
        if (e.key === 'p' || e.key === 'P') {
          togglePinyinVisibility();
        }

        if (state.activeMode === 'flashcards') {
          if (e.code === 'Space') {
            e.preventDefault();
            flipFlashcard();
          } else if (e.code === 'ArrowRight') {
            e.preventDefault();
            nextFlashcard();
          } else if (e.code === 'ArrowLeft') {
            e.preventDefault();
            prevFlashcard();
          }
        }
      });
    }

    /* Initialize App */
    function init() {
      applyTheme(state.theme);
      renderLessonPills();
      updateFilteredViews();
      setupEventListeners();
    }

    document.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
"""

full_html = html_template.replace('__VOCAB_PLACEHOLDER__', vocab_json_str)

with open('/Users/quocthong248/.gemini/antigravity/scratch/hsk-vocab-app/index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated index.html successfully! File size:", len(full_html), "bytes")
