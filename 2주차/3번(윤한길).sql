-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' and NAME LIKE '%el%'
ORDER BY NAME;


-- 대소문자 구분 하려면
-- NAME LIKE BINARY '%el%' or NAME LIKE BINARY '%El%'
-- BINARY 옵션 추가 -> case-sensitive
-- When we use BINARY, then mysql compare data byte-by-byte. Without BINARY it compares data character-by-character.

-- Case sensitive example
--SELECT *
--FROM TABLE
--WHERE Name collate SQL_Latin1_General_CP1_CS_AS like '%hospitalist%'

-- Case insensitive example
--SELECT *
--FROM TABLE
--WHERE Name collate SQL_Latin1_General_CP1_CI_AS like '%hospitalist%'