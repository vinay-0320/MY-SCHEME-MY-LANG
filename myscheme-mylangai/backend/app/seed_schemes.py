"""Idempotent starter catalog of official-source leads; never auto-verifies eligibility.
Run: docker compose exec backend python -m app.seed_schemes
"""
from datetime import datetime, timezone
from sqlalchemy import select
from .main import Session, Scheme

RECORDS = [
 ('ka-gruha-lakshmi','Gruha Lakshmi','Karnataka','Women and Child Development','Karnataka household-support scheme for eligible women identified as household heads. Check current ration-card, tax and other exclusions in the linked government study before applying.','https://fpibengaluru.karnataka.gov.in/uploads/media_to_upload1762775113.pdf'),
 ('ka-gruha-jyothi','Gruha Jyothi','Karnataka','Energy Department','Electricity benefit for eligible domestic consumers in Karnataka; usage caps and account requirements apply. Check current rules before claiming a benefit.','https://fpibengaluru.karnataka.gov.in/uploads/media_to_upload1762775086.pdf'),
 ('ka-anna-bhagya','Anna Bhagya','Karnataka','Food, Civil Supplies and Consumer Affairs','Food-security support associated with qualifying ration-card households; benefit delivery and exclusions may change.','https://fpibengaluru.karnataka.gov.in/uploads/media_to_upload1762775113.pdf'),
 ('ka-shakti','Shakti Scheme','Karnataka','Transport Department','Fare-free eligible bus travel for qualifying Karnataka residents; service and identity conditions must be checked.','https://fpibengaluru.karnataka.gov.in/storage/pdf-files/Technical%20Reports/FinalcopyofFiscaleffectsofShaktiScheme_04072024.pdf'),
 ('ka-yuva-nidhi','Yuva Nidhi','Karnataka','Skill Development, Entrepreneurship and Livelihood','Unemployment assistance initiative for qualifying Karnataka graduates and diploma holders. Review current eligibility and registration conditions.','https://www.yuvaudyogasethu.karnataka.gov.in/en/job-portal'),
 ('in-pm-kisan-maandhan','Pradhan Mantri Kisan Maandhan Yojana','Central','Ministry of Agriculture and Farmers Welfare','Contributory pension scheme for qualifying small and marginal farmers; age, landholding and exclusion conditions require review.','https://www.myscheme.gov.in/schemes/pmkmdy'),
 ('in-pmay-urban','Pradhan Mantri Awas Yojana - Urban','Central','Ministry of Housing and Urban Affairs','Urban housing assistance with income and housing-ownership conditions; component-specific rules must be reviewed.','https://www.myscheme.gov.in/schemes/pmay-u'),
 ('in-ab-pmjay','Ayushman Bharat PM-JAY','Central','National Health Authority','Health coverage initiative for eligible households; check beneficiary identification and current local implementation.','https://www.myscheme.gov.in/hi/schemes/ab-pmjay'),
 ('in-pm-kisan','PM-KISAN Samman Nidhi','Central','Ministry of Agriculture and Farmers Welfare','Income support for qualifying landholding farmer families, subject to exclusions and government verification.','https://pmkisan.gov.in/'),
 ('in-e-shram','e-Shram Worker Registration','Central','Ministry of Labour and Employment','National registration portal for qualifying unorganised workers; registration itself is not a cash benefit.','https://eshram.gov.in/faqs'),
]

def main():
    added=skipped=0
    with Session() as db:
        for ident,name,state,department,description,source_url in RECORDS:
            if db.get(Scheme,ident):
                skipped+=1
                continue
            db.add(Scheme(id=ident,name=name,state=state,department=department,description=description,source_url=source_url,application_url=None,eligibility={},documents=[],status='unverified',verified_at=None))
            added+=1
        db.commit()
    print(f'Catalog seeded: {added} new; {skipped} already present. All new records are UNVERIFIED; no eligibility assertions made.')

if __name__=='__main__':
    main()