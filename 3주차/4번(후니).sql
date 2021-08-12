-- 코드를 입력하세요
# SELECT * FROM places;

    # SELECT 
    #     *
    # FROM 
    #     places
    # GROUP BY 
    #     HOST_ID
    # HAVING 
    #     COUNT(HOST_ID) > 1
    # ORDER BY 
    #     ID
        
SELECT
    pla.ID, pla.NAME, pla.HOST_ID
FROM
    places pla
    ,
    (SELECT 
        *
    FROM 
        places
    GROUP BY 
        HOST_ID
    HAVING 
        COUNT(HOST_ID) > 1
    ) sorted
WHERE
    pla.HOST_ID = sorted.HOST_ID
ORDER BY
    pla.ID
