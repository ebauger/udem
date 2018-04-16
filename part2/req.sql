USE udem_part2;
#requete1
SELECT
  w.name
  count(p.website_id)
FROM
  Pages as p, Websites as w
LEFT JOIN
  Pages ON w.id = p.website_id;

#requete2
FROM
  Tags as t
  Websites as w
  Pages as p

#requete3

#requete4 todo create procedure
SELECT
  COUNT(id)
FROM
  Pages as p,
  States as s
WHERE
  (p.url LIKE '%/products/%') AND
  (TIMEDIFF(s.last_verification, 'date')) AND
  (s.state = 'stateName')
;