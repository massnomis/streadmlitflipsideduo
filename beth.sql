SELECT
  DATE_TRUNC('day', block_timestamp) AS day,
   count(tx_id) as COUNTs,	
  sum( (msg_value:execute_msg:send:amount /POW(10,6))) as SUMDEPANC,
  avg( (msg_value:execute_msg:send:amount /POW(10,6))) as AVGDEPANC, 
  median( (msg_value:execute_msg:send:amount /POW(10,6))) as MEDDEPANC
FROM terra.msgs
  WHERE msg_value:execute_msg:send:msg:deposit_collateral IS NOT NULL
  and msg_value:contract::string =  'terra1dzhzukyezv0etz22ud940z7adyv7xgcjkahuun'

  and tx_status = 'SUCCEEDED'
group by day
order by day desc



