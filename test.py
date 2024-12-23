# def test_exception():
#     try:
#         a = 0/0
#     except RuntimeError as error:
#         raise exception(error)  # type: ignore
#     else:
#         print("there is no exception, the try function executed successfully")
#     finally:
#         print("everything has been cleaned up after run try function!!")

# test_exception()


def test_exception(n):
    try:
        a = 0 / n  # This will raise ZeroDivisionError
    except ZeroDivisionError as error:  # Catching the correct exception
        print(f"Caught an exception: {error}")
        raise RuntimeError(
            "A runtime error occurred due to division by zero") from error
    else:
        # This will only execute if no exception occurs in the try block
        print("There is no exception, the try function executed successfully")
    finally:
        # This will always execute, no matter what happens in try/except/else
        print("Everything has been cleaned up after running the try function!!")


# Test the function
test_exception(1)



with CTE as(
select num_users, 
row_number() over(order by num_users)
from search_frequency
)

select 
case 
when (select max(row_number) from CTE)%2=1 then (select num_users from CTE where row_number=(select max(row_number +1)/2 from CTE))
else (SELECT round(avg(num_users),2)
from CTE
WHERE row_number IN (
    (SELECT MAX(row_number) / 2 FROM CTE),
    (SELECT MAX(row_number) / 2 + 1 FROM CTE)))
AS median
from CTE