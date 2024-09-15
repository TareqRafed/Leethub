# Write your MySQL query statement below

SELECT firstName, lastName, a.city, a.state from Person left join Address a on a.personId = Person.personId;