Use Nummr;
SELECT * FROM cpichina;
SELECT * FROM cpiindo;
SELECT * FROM cpius;
SELECT * FROM oilprice;

SELECT oilprice.Date, oilprice.Close, cpichina.CPI_CH 
FROM cpichina 
RIGHT JOIN oilprice 
ON cpichina.Date = oilprice.Date;