SELECT s.code AS [Código], c.razao_social AS [Razão Social], p.number AS Telefone
  FROM Client AS c
  INNER JOIN State AS s ON c.id_state = s.id 
  INNER JOIN ClientPhone AS cf ON cf.id_client = c.id
  INNER JOIN Phone AS p on p.id = cf.id_phone
  WHERE s.code = 'SP'
