#三期申请书
noa_3yl = """SELECT	
 format(count(id),0) 三期申请案件数
FROM	
 insurance_claim ic
WHERE	
	product_code IN ( 'ninghuibao-2023-picc-standard','ninghuibao-2023-picc-upgrade') 
	and status not in ('CANCELED','NOT_SUBMITTED')"""
#三期结案数
nocc_3yl ="""SELECT	
format(count(ID),0) 三期结案数
FROM	
	insurance_claim ic
WHERE	
	product_code IN ( 'ninghuibao-2023-picc-standard','ninghuibao-2023-picc-upgrade') 
	--AND CONVERT_TZ( issue_time, '+00:00', '+08:00' ) < '2023-05-30 15:23:59' 
	and status in ('INSURANCE_COMPANY_ACCEPTED',
	'INSURANCE_COMPANY_ANNUL_OR_REFUSED',
	'INSURANCE_COMPANY_COMPLETED',
	'INSURANCE_COMPANY_REJECTED',
	'SYSTEM_AUDITED',
	'SYSTEM_REJECTED',
	'WAIT_INSURANCE_COMPANY_AUDITED',
	'WAIT_REVIEW')
"""
#三期赔付情况:赔付数量,赔付金额,赔付率,人均赔付
nocs_tcp_ir_pcc_3yl = """SELECT	
format(count(ic.ID),0) 三期赔付数量,
format(count(distinct ic.insured_credential_number),0) 三期赔付人数,
format(sum(case when ica.actual_paid_amount >0 then ica.actual_paid_amount else ica.total_claim_amount end ),2) as 赔付金额,
format(sum(case when ica.actual_paid_amount >0 then ica.actual_paid_amount else ica.total_claim_amount end )*100/181099368,2)  as 赔付率,
format(sum(case when ica.actual_paid_amount >0 then ica.actual_paid_amount else ica.total_claim_amount end )/count(distinct ic.insured_credential_number),2) as 人均赔付
FROM	
	insurance_claim ic
	join insurance_claim_amount ica on ica.claim_id = ic.id 
WHERE	
	product_code IN ( 'ninghuibao-2023-picc-standard','ninghuibao-2023-picc-upgrade') 
	and status in ('INSURANCE_COMPANY_ACCEPTED',
	'INSURANCE_COMPANY_ANNUL_OR_REFUSED',
	'INSURANCE_COMPANY_COMPLETED',
	'WAIT_INSURANCE_COMPANY_AUDITED',
	'wait_review'
	)
	and ica.delete_time is null
	and ica.total_claim_amount>0"""
#三期平均减负率
aiwlr_3yl="""SELECT
	format(avg(减负率)*100,2) as 人均减负率
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
			product_code IN ( 'ninghuibao-2023-picc-standard','ninghuibao-2023-picc-upgrade' ) 
			AND STATUS IN ( 'INSURANCE_COMPANY_ACCEPTED', 'INSURANCE_COMPANY_ANNUL_OR_REFUSED', 'INSURANCE_COMPANY_COMPLETED', 'WAIT_INSURANCE_COMPANY_AUDITED', 'wait_review' ) 
			AND ica.total_claim_amount > 0 
			AND ica.delete_time IS NULL 
		) 
		AND product_code IN ( 'ninghuibao-2023-picc-standard','ninghuibao-2023-picc-upgrade' ) 
		AND STATUS IN ( 'INSURANCE_COMPANY_ACCEPTED', 'INSURANCE_COMPANY_ANNUL_OR_REFUSED', 'INSURANCE_COMPANY_COMPLETED', 'WAIT_INSURANCE_COMPANY_AUDITED', 'wait_review', 'SYSTEM_AUDITED' ) 
		AND ica.delete_time IS NULL 
	GROUP BY
	ic.insured_credential_number 
	)t"""
#三期医疗费用情况:总费用,统筹费用,个人负担
tme_ssp_ib_3yl="""	SELECT	
sum(ici.amount) as 总费用,
sum(fund_paid_amount+serious_illness_paid+serious_illness_insurance_paid+civil_affair_subsidy_paid) as 统筹,
sum(self_paid_amount+self_care_amount+self_amount+self_amount_supply) 个人负担
FROM	
	insurance_claim ic
	join insurance_claim_medical icm on icm.claim_id=ic.id and icm.delete_time is null 
	join insurance_claim_invoice ici on ici.claim_medical_id = icm.id and ici.delete_time is null and ici.`status` = 'SAVED'
WHERE	
	product_code IN ( 'ninghuibao-2023-picc-standard','ninghuibao-2023-picc-upgrade') 
	and ic.status  not in ('CANCELED','NOT_SUBMITTED')"""
#二期同期减负率
ir_2_3yl="""SELECT	
format(sum(case when ica.actual_paid_amount >0 then ica.actual_paid_amount else ica.total_claim_amount end )*100/87300081,2) as 二期同期赔付率
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
	and ica.total_claim_amount>0
	and CONVERT_TZ( issue_time, '+00:00', '+08:00' ) <date_sub(now(),interval 1 year)"""

jwz_fjwz_tca_3yl="""SELECT
	case when icm.past_symptom=1 then '既往症' else '非既往症' end as 是否既往症 ,
format(sum(case when ica.actual_paid_amount >0 then ica.actual_paid_amount else ica.total_claim_amount end ),2) as 赔付金额,
format(sum(case when ica.actual_paid_amount >0 then ica.actual_paid_amount else ica.total_claim_amount end )*100/181099368,2) as 赔付金额率,
format(sum(self_paid_claim_amount),2)  责任一赔付,
format(sum(self_paid_claim_amount)*100/181099368,2) 责任一赔付率,
format(sum(self_care_claim_amount),2)  责任二赔付,
format(sum(self_care_claim_amount)*100/181099368,2) 责任二赔付率
FROM	
	insurance_claim ic
	join (select claim_id ,max(past_symptom) as past_symptom from insurance_claim_medical where delete_time is null  group by claim_id) icm on ic.id =icm.claim_id
	join insurance_claim_amount ica on ica.claim_id=ic.id and ica.delete_time is null 
WHERE	
	product_code IN ( 'ninghuibao-2023-picc-standard','ninghuibao-2023-picc-upgrade') 
	and ic.status   in ('INSURANCE_COMPANY_ACCEPTED',
	'INSURANCE_COMPANY_ANNUL_OR_REFUSED',
	'INSURANCE_COMPANY_COMPLETED',
	'WAIT_INSURANCE_COMPANY_AUDITED',
	'wait_review'
	)
	and ica.total_claim_amount>0
	group by icm.past_symptom
order by 是否既往症"""