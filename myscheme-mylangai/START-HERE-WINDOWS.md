# MyScheme MyLangAI — Windows setup (development version 0.2)

## What this update changes
- Kannada, Hindi, Tamil, Telugu, and English explain **missing verified data** in their own language (not an AI answer).
- `/api/capabilities` reports configured providers without exposing secrets.
- Admin-only manual verification endpoint for curated records.
- Docker Compose forwards `AI_PROVIDERS` and `GEMINI_MODEL` to the backend.

**Not yet included:** automatically verified government scheme records, automatic ingestion, real voice, OCR, fully tested 23-language AI support. An AI API key by itself will not fill the scheme database.

## Upgrade your existing Windows project
1. Stop Docker with `Ctrl+C` in the running terminal.
2. Back up your current project folder.
3. Extract this ZIP into a **new** folder. Do not copy the `.env` file into Git or upload it anywhere.
4. Open PowerShell inside the extracted `myscheme-mylangai` folder.
5. Copy `.env.example` to `.env` if you are starting fresh.
6. Optionally edit `.env` to add `GEMINI_API_KEY=...` (do not share the key).
7. Run `docker compose up --build`.
8. Open http://localhost:3000 and http://localhost:8000/api/capabilities.

## API key
Get a Gemini key from https://aistudio.google.com/api-keys . Provider quotas, model names, and billing may change. Never put the key in frontend files. Restart the backend after changing `.env` using `docker compose up -d --force-recreate backend`.

## Adding real scheme information
Only administrators can POST `/api/admin/schemes` with an `x-admin-key` header. Records start as `unverified`. Admins must check official government pages and eligibility conditions before calling `/api/admin/schemes/{id}/verification` with `{ "verified": true, "verification_note": "..." }`. This development endpoint does **not** persist verification notes, so use external records until an audit table is implemented. Never mark an unreviewed scheme verified.

The site is an independent development project, not an official government service. Government authorities make final eligibility decisions.
