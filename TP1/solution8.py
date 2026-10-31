def describe(*number,decimal=2,label="data"):
    if not number:
        print(f"No {label} no value")
        return None
    count=len(number)
    minimum=min(number)
    maximum=max(number)
    mean=sum(number)/count
    min_str = (
        f"{minimum:.{decimal}f}" 
        if isinstance(minimum, float) 
        else str(minimum)
        )
    max_str = (
    f"{maximum:.{decimal}f}"
    if isinstance(maximum, float)
    else str(maximum)
    )
    print(f"{label}: n={count}, min={min_str}, max={max_str}, mean={mean:.{decimal}f}")
    return (count, minimum, maximum, mean)

def make_tag(text, **styles):
    attributes = " ".join(f'{key}="{value}"' for key, value in styles.items())
    if attributes:
        return f'<span {attributes}>{text}</span>'
    return f'<span>{text}</span>'

square = lambda x: x**2
adult_age = lambda age: age >= 18
describe(12, 7, 30, 4)
describe(3.14159, 2.71828, decimal=3, label="Constants")
describe()
print(make_tag("Hello!", color= "red;", size="14"))
print(square(9), adult_age(17), adult_age(21))

    