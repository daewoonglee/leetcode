"""
delete p1 from person p1, person p2
where p1.id > p2.id and p1.email = p2.email


delete from person p1
where p1.id not in (select * from (select min(id) from person
                    group by email) as p2)


with cte as
(
    select id,email, row_number() over(
    partition by email order by id) as dups from Person
)
delete from person where id in (select id from cte where dups > 1);
"""