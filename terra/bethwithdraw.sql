--
-- https://app.flipsidecrypto.com/velocity/queries/770c4049-a3b7-45b0-9977-88df8f197ed9

with a as 
  		(
				select
                    (DATE_TRUNC('day', block_timestamp)) as dayz,
                    (EVENT_ATTRIBUTES:"0_amount") / pow(10,6) as amountz,
                    (EVENT_ATTRIBUTES:"from"::string) as whomz,
  					tx_id
				from 
              		terra.msg_events
    			where 
              		(EVENT_ATTRIBUTES:"0_action"::string) = 'burn'
              	AND
              		(EVENT_ATTRIBUTES:"0_contract_address"::string) = 'terra1dzhzukyezv0etz22ud940z7adyv7xgcjkahuun'
		)
,
b as   
		(
				select 
  					dayz,
                    avg(amountz),
                    sum(amountz),
                    min(amountz),
                    max(amountz),
                    median(amountz),
  					count(distinct(whomz)) as whomz_count,
  					count(distinct(tx_id)) as tx_count
				from a
				group by dayz
 				order by dayz desc
        )
  
SELECT * FROM B
