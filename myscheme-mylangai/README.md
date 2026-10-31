# MyScheme MyLangAI

An independent development preview of a multilingual Indian government scheme assistant. **Not an official government service.**

## Current implementation
- Responsive Next.js application with chat, scheme explorer, eligibility form, PDF text extraction, language selector, and consent checkbox.
- FastAPI service with PostgreSQL-backed scheme records, structured rule evaluation, protected admin creation endpoint, feedback endpoint, and generated OpenAPI docs.
- Configurable OpenAI, Gemini and Anthropic text adapters (API keys required), with sequential fallback. Only verified scheme records are passed as evidence.
- Docker Compose for PostgreSQL, Redis, frontend and backend; simple unit tests and GitHub CI.

## Quick start
1. Install Docker and Docker Compose.
2. Copy `.env.example` to `.env` and set a strong `ADMIN_API_KEY`. AI keys are optional.
3. Run `docker compose up --build` from this directory.
4. Visit http://localhost:3000; API docs: http://localhost:8000/docs.
5. Use `POST /api/admin/schemes` with header `x-admin-key` to add records from official sources. New records default to `unverified`; a separate verification workflow is not implemented. No example schemes are preloaded to avoid fabricated data.

## Important limitations
This is an initial runnable foundation, **not** the fully complete production system in the master prompt. No automated official-source crawling, multilingual embeddings/pgvector retrieval, migrations, comprehensive state coverage, automatic language detection, speech, image OCR, production RBAC, Terraform, refresh scheduler, 100-case evaluation or real-world source verification. Language selection covers 22 scheduled languages and English but output quality and voice capability are not verified. The API does not store chat profiles; do not upload sensitive documents. Browser access requires the backend running locally.

## Testing
`cd backend && pip install -r requirements.txt && PYTHONPATH=. pytest -q`

## Deployment
Local Docker Compose only. Do not deploy to public internet without authentication, rate limiting, TLS, privacy/security review, and authoritative scheme verification.

## License
All rights reserved. No open-source license is granted. Public GitHub repositories may still be viewed and forked under GitHub platform terms.
