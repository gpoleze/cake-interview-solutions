# [Word Cloud Data](https://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiNDc3NDM4NCIsImRlbGl2ZXJ5X2lkIjoiY2Nhc3Zvc21tcWF4MGhtOGMyM3ciLCJ1cmwiOiJodHRwczovL3d3dy5pbnRlcnZpZXdjYWtlLmNvbS9xdWVzdGlvbi93b3JkLWNsb3VkP3V0bV9zb3VyY2U9d2Vla2x5X2VtYWlsXHUwMDI2dXRtX2NhbXBhaWduPXdlZWtseV9lbWFpbFx1MDAyNnV0bV9tZWRpdW09ZW1haWxcdTAwMjZfX3M9cGY3MTE1M3NtMnFmemFzZzl5MjRcdTAwMjZ1dG1fc291cmNlPWRyaXBcdTAwMjZ1dG1fbWVkaXVtPWVtYWlsXHUwMDI2dXRtX2NhbXBhaWduPUludGVydmlldytDYWtlK1dlZWtseStQcm9ibGVtKyUyMzMxMCUzQStXb3JkK0Nsb3VkK0RhdGEifQ)
### You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a dictionary , where the keys are words and the values are the number of times the words occurred.

**Think about capitalized words**. For example, look at these sentences:

    'After beating the eggs, Dana read the next step:'
    'Add milk and eggs, then add flour and sugar.'
What do we want to do with "After", "Dana", and "add"? In this example, your final dictionary should include one "Add" or "add" with a value of 22. Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.

>You could make a reasonable argument to use regex in your solution. We won't, mainly because performance is difficult to measure and [can get pretty bad](http://blog.codinghorror.com/regex-performance/).