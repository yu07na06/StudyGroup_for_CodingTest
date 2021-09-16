SELECT * FROM PLACES /* ID, NAME, HOST_ID 모두 선택하므로 전체 선택(*) */
/* HOST_ID의 조건만 보면 되므로 */
WHERE HOST_ID IN (SELECT HOST_ID 
                 FROM PLACES
                 GROUP BY HOST_ID /* 중복된 HOST_ID를 합침 */
                 HAVING COUNT(*)>1) /* 중복된 개수가 2개 이상이라면, HOST_ID를 선택 */
