## Purpose
This file gives concise, actionable guidance for AI coding agents working on this repository so they can be productive immediately.

## Big picture
- Single small Streamlit web app: `streamlit_web.py` is the app entrypoint. See [streamlit_web.py](streamlit_web.py#L1-L40).
- Prediction pipeline is delegated to a helper module imported as `from utils import pred_pipe` and a model file referenced by `MODEL_PATH = "NLP/sentiment_classifier.pkl"`.
- Typical data flow: user text -> `pred_pipe(text, MODEL_PATH)` -> label string (e.g. "Positive"/"Negative") -> displayed via Streamlit UI.

## What to look for first
- `streamlit_web.py`: app structure, UI widgets (`st.title`, `st.text_area`, `st.button`), and how results are rendered.
- `utils.py` (expected): contains `pred_pipe()` implementation. If missing, search for prediction wrappers or a `models/` or `NLP/` folder.
- Model artifacts: path referenced by `MODEL_PATH` (adjust only if a trained artifact exists in the repo or an external storage location).

## Common agent tasks & conventions
- Run the app locally: `streamlit run streamlit_web.py` from the repo root.
- Minimal edits to UI: keep Streamlit calls (title, text_area, button) in the top-level script to preserve simple run semantics.
- Prediction call pattern: always pass the input string and model path to `pred_pipe`. Example call in repo: `pred_pipe(user_input, MODEL_PATH)`.
- Styling: app uses inline HTML via `st.markdown(..., unsafe_allow_html=True)` for colored output — preserve this pattern if modifying result rendering.

## When adding code
- If you add helper modules, import them from top-level names (e.g., `from utils import ...`) or update `PYTHONPATH`/package layout; prefer adding a small package (folder with `__init__.py`) rather than altering the run command.
- Keep model path references explicit as `MODEL_PATH` constants in files that use them.

## Debugging hints
- If `utils` or `NLP/sentiment_classifier.pkl` are missing, run a workspace search for `pred_pipe` or `sentiment_classifier` to locate alternate locations.
- Common exception sources: missing model file or incompatible model format. Reproduce locally by calling `pred_pipe()` in a short REPL script before changing UI.

## Tests & CI
- There are no discoverable tests in the repo. If you add tests, place them under `tests/` and prefer lightweight unit tests for `pred_pipe` and model-loading logic.

## External integrations
- The app depends on `streamlit` and whatever libraries `pred_pipe` uses (likely sklearn/pickle/joblib). Do not add heavy runtime dependencies without documenting install steps.

## Files to reference in code reviews
- [streamlit_web.py](streamlit_web.py#L1-L40) — main app
- `utils.py` — expected prediction helpers (create if absent)
- `NLP/sentiment_classifier.pkl` — model artifact path referenced by the app

## Quick checklist for PRs by an AI agent
- Confirm `pred_pipe` exists and its API matches `pred_pipe(text, model_path)`.
- Ensure `MODEL_PATH` points to an existing artifact or update README documenting how to obtain/create it.
- Preserve Streamlit runtime command (`streamlit run streamlit_web.py`) and minimal top-level script shape.
- Keep changes scoped: small helper files, not broad refactors unless requested.

---
If anything above is unclear or you'd like me to expand examples (for instance, a suggested `utils.py` stub or a `requirements.txt`), tell me which part to refine and I'll update this file.
