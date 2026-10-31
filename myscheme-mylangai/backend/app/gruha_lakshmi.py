"""Preliminary Gruha Lakshmi screening; not an official eligibility determination."""
from pydantic import BaseModel
from typing import Literal
Answer = Literal['yes','no','unknown']
class GruhaLakshmiAnswers(BaseModel):
    karnataka_resident: Answer = 'unknown'
    ration_card_type: Literal['AAY','BPL','APL','other','unknown'] = 'unknown'
    household_head: Answer = 'unknown'
    applicant_or_spouse_income_taxpayer: Answer = 'unknown'
    applicant_or_spouse_gst_filer: Answer = 'unknown'
    aadhaar_kyc_completed: Answer = 'unknown'
    mobile_sim_in_beneficiary_name: Answer = 'unknown'

def screen(a: GruhaLakshmiAnswers):
    core = {
        'karnataka_resident': a.karnataka_resident,
        'eligible_ration_card': 'yes' if a.ration_card_type in ('AAY','BPL','APL') else ('unknown' if a.ration_card_type=='unknown' else 'no'),
        'household_head': a.household_head,
        'income_tax_exclusion': 'no' if a.applicant_or_spouse_income_taxpayer=='yes' else ('yes' if a.applicant_or_spouse_income_taxpayer=='no' else 'unknown'),
        'gst_exclusion': 'no' if a.applicant_or_spouse_gst_filer=='yes' else ('yes' if a.applicant_or_spouse_gst_filer=='no' else 'unknown'),
    }
    failed = [k for k,v in core.items() if v=='no']
    missing = [k for k,v in core.items() if v=='unknown']
    status = 'core_condition_not_met' if failed else 'more_information_needed' if missing else 'core_conditions_appear_met'
    return {'status':status,'failed':failed,'missing':missing,
      'kyc':{'aadhaar_kyc_completed':a.aadhaar_kyc_completed,
             'mobile_sim_in_beneficiary_name':a.mobile_sim_in_beneficiary_name,
             'mobile_rule_status':'unverified_report_not_used_for_eligibility'},
      'warning':'Preliminary educational screening only. The scheme record remains unverified; government authorities decide eligibility and DBT payment status. Confirm current KYC requirements with an authorised government centre.',
      'official_information':'https://sevasindhugs.karnataka.gov.in/'}
