
USE udem_part2;

/*
requete1
Tous les sites incluant le nombre de pages de chacun;
 */
-- DISTINCT I presume each website are unique
SELECT
  w.name,
  count(pu.website_id) AS page_count
FROM website AS w
LEFT JOIN page_url AS pu
  ON w.id = pu.website_id;

/*
requete2 
Toutes les étiquettes incluant le nombre de sites 
et de pages associées à chacune;*/

-- I presume each tag have minimum association with a page or website; if not, no association on this table.
SELECT
  t.name_fr, t.name_en,
  count(w.id) as website_count,
  count(pu.id) as page_count
FROM
  tag_website_page_url AS twpu
LEFT JOIN tag as t
  ON twpu.tag_id = t.id
LEFT JOIN website AS w
  ON twpu.page_id = p.id
LEFT JOIN page_url AS pu
  ON twpu.website_id = w.id;
/*
requete3 
Toutes les pages d'un site incluant le nombre de versions de contenu disponibles
et la taille totale de toutes les versions de chacune;
*/
SELECT
  pu.url_path,
  count(hv.id),
  LENGTH(hv.html) as size_kb -- 
FROM page_url as pu
LEFT JOIN html_version as hv
  ON pu.id = hv.page_url_id
WHERE pu.id IN (
  SELECT DISTINCT id
  FROM website
  WHERE root_url = @search
);

/*
requete4
Combien de pages d'un site donné dont l'URL inclut ​"/products/"​ 
ont du contenu plus récent que le moment X 
et un état spécifique.
*/
SELECT
  COUNT(id)
FROM page_url as pu
LEFT JOIN page_status as ps
  ON pu.id IN (
    SELECT id
    FROM page_status
    WHERE page_status.description_name = @state_name
  )
WHERE pu.id IN (
  SELECT DISTINCT id
  FROM website
  WHERE root_url = @exact_url
) AND ((pu.url_path LIKE '%/products/%'))
  AND (TIMEDIFF(pu.last_check, @exact_date))