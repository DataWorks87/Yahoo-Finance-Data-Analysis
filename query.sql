select n.company, n.hour, n2.ts as date_time, n.hourly_high

from (
    select name as company, hour(date_add('hour',-4,cast(ts as timestamp))) as hour, max(high) as hourly_high
    from  "ydata"."22"
    group BY 1, 2
    order BY 1, 2
     ) n,
  "ydata"."22" n2
 
where n.company=n2.name and  n.hour = hour(date_add('hour',-4,cast(n2.ts as timestamp))) and n.hourly_high = n2.high
 
order by 1, 3
;