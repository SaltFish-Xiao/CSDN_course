noa = """SELECT
 count(id) 二期申请案件数
FROM
 insurance_claim ic
WHERE
	product_code IN ( 'ninghuibao-2022-picc-standard')
	and status not in ('CANCELED','NOT_SUBMITTED') """
nocc = """SELECT
count(ID) 二期结案数
FROM
	insurance_claim ic
WHERE
	product_code IN ( 'ninghuibao-2022-picc-standard')
	and status in ('INSURANCE_COMPANY_ACCEPTED',
	'INSURANCE_COMPANY_ANNUL_OR_REFUSED',
	'INSURANCE_COMPANY_COMPLETED',
	'INSURANCE_COMPANY_REJECTED',
	'SYSTEM_AUDITED',
	'SYSTEM_REJECTED',
	'WAIT_INSURANCE_COMPANY_AUDITED',
	'WAIT_REVIEW'
	) """
nocs = """SELECT
count(distinct ic.ID) 二期赔付数量
FROM
	insurance_claim ic join insurance_claim_amount ica on ic.id = ica.claim_id
WHERE
	product_code IN ( 'ninghuibao-2022-picc-standard')
	and ic.status in ('INSURANCE_COMPANY_ACCEPTED',
	'INSURANCE_COMPANY_ANNUL_OR_REFUSED',
	'INSURANCE_COMPANY_COMPLETED',
	'WAIT_INSURANCE_COMPANY_AUDITED',
	'wait_review')
	 and ica.total_claim_amount>0"""
tcp_ir_pcc = """SELECT	
sum(case when ica.actual_paid_amount >0 then ica.actual_paid_amount else ica.total_claim_amount end ) as 赔付金额,
sum(case when ica.actual_paid_amount >0 then ica.actual_paid_amount else ica.total_claim_amount end )/87300081  as 赔付率,
sum(case when ica.actual_paid_amount >0 then ica.actual_paid_amount else ica.total_claim_amount end )/count(distinct ic.insured_credential_number) as 人均赔付
FROM	
	insurance_claim ic
	join insurance_claim_amount ica on ica.claim_id = ic.id 
WHERE	
	product_code IN ( 'ninghuibao-2022-picc-standard') 
	and status in ('INSURANCE_COMPANY_ACCEPTED',
	'INSURANCE_COMPANY_ANNUL_OR_REFUSED',
	'INSURANCE_COMPANY_COMPLETED',
	'WAIT_INSURANCE_COMPANY_AUDITED',
	'wait_review'
	)
	and ica.delete_time is null
	and ica.total_claim_amount>0"""
aiwlr="""SELECT
	avg(减负率)
FROM
	(
	SELECT
		ic.insured_credential_number,
		sum( CASE WHEN ica.actual_paid_amount > 0 THEN ica.actual_paid_amount ELSE ica.total_claim_amount END )/ sum( ica.self_burden_amount ) AS 减负率
	FROM
		insurance_claim ic
		JOIN insurance_claim_amount ica ON ica.claim_id = ic.id
	WHERE
		ic.insured_credential_number IN (
		SELECT
			ic.insured_credential_number
		FROM
			insurance_claim ic
			JOIN insurance_claim_amount ica ON ica.claim_id = ic.id
		WHERE
			product_code IN ( 'ninghuibao-2022-picc-standard' )

			AND STATUS IN ( 'INSURANCE_COMPANY_ACCEPTED', 'INSURANCE_COMPANY_ANNUL_OR_REFUSED', 'INSURANCE_COMPANY_COMPLETED', 'WAIT_INSURANCE_COMPANY_AUDITED', 'wait_review' )
			AND ica.total_claim_amount > 0
			AND ica.delete_time IS NULL
		)
		AND product_code IN ( 'ninghuibao-2022-picc-standard' )
		AND STATUS IN ( 'INSURANCE_COMPANY_ACCEPTED', 'INSURANCE_COMPANY_ANNUL_OR_REFUSED', 'INSURANCE_COMPANY_COMPLETED', 'WAIT_INSURANCE_COMPANY_AUDITED', 'wait_review', 'SYSTEM_AUDITED' )
		AND ica.delete_time IS NULL
	GROUP BY
	ic.insured_credential_number )t"""
tme_ssp_ib="""	SELECT	
sum(ici.amount) as 总费用,
sum(fund_paid_amount+serious_illness_paid+serious_illness_insurance_paid+civil_affair_subsidy_paid) as 统筹,
sum(self_paid_amount+self_care_amount+self_amount) 个人负担
FROM	
	insurance_claim ic
	join insurance_claim_medical icm on icm.claim_id=ic.id and icm.delete_time is null 
	join insurance_claim_invoice ici on ici.claim_medical_id = icm.id and ici.delete_time is null and ici.`status` = 'SAVED'
WHERE	
	product_code IN ( 'ninghuibao-2022-picc-standard') 
	and ic.status  not in ('CANCELED','NOT_SUBMITTED')"""
ir_1="""SELECT	
sum(case when ica.actual_paid_amount >0 then ica.actual_paid_amount else ica.total_claim_amount end )/40668409  as 赔付率
FROM	
	insurance_claim ic
	join insurance_claim_amount ica on ica.claim_id = ic.id 
WHERE	
	product_code IN ( 'ninghuibao-2021-picc-standard','ninghuibao-2021-picc-upgrade') 
	and status in ('INSURANCE_COMPANY_ACCEPTED',
	'INSURANCE_COMPANY_ANNUL_OR_REFUSED',
	'INSURANCE_COMPANY_COMPLETED',
	'WAIT_INSURANCE_COMPANY_AUDITED',
	'wait_review'
	)
	and ica.delete_time is null
	and ica.total_claim_amount>0
	AND CONVERT_TZ( issue_time, '+00:00', '+08:00' ) <date_sub(now(),interval 1 year)"""