## Student Funnel Enrollment System


## Requirements

This system has been developed based in the following requirements:

- Get list of all the funnel status
- Create new funnel Status
- Update the Existing Funnel Status
- Delete Existing funnel Status
- Create new Customer (student)
- Update the Status and details of the Student
- Retrieve 50 latest logs from the system, response should be paginated for see the older logs.



## APIs of the System

APIs has been developed based on the requirements and each API serves a different purposes

## Support

To Up and Running the Application make sure you have the following versions


**Python:** Python 3.8.6 or Above

**Django:** 4.2.13 or Above

## Run Locally

Clone the project 

```bash
  git clone https://github.com/RealAbishan/school_enrolment_funnel.git
```

Go to the project directory

```bash
  cd schoole_enrolment_funnel
```

## APIs of the System
- Get list of all the funnel status
```http
  GET http://127.0.0.1:8000/api/funnel-status/
```

- Create new funnel Status
```http
  POST http://127.0.0.1:8000/api/funnel-status/
```

- Update the Existing Funnel Status
```http
  UPDATE http://127.0.0.1:8000/api/funnel-status/
```

- Delete Existing funnel Status
```http
  DELETE http://127.0.0.1:8000/api/funnel-status/
```

- Create new Customer (student)
```http
  POST http://127.0.0.1:8000/api/students/
```
- Update the Status and details of the Student
```http
  UPDATE http://127.0.0.1:8000/api/students/:id/update_status/
```
- Retrieve 50 latest logs from the system, response should be paginated for see the older logs.
```http
  GET http://127.0.0.1:8000/api/logs/
```
- Get Customer(Student) details 
```http
  GET http://127.0.0.1:8000/api/
```


## Related

Use the following cURL for API testing

[Link to the cURL](~https://documenter.getpostman.com/view/14042982/2sA3JT2xgz)


## References

Following websites and YouTube channels has been reffed during the development stage

- [@Geeksforgeeks](https://www.geeksforgeeks.org/adding-pagination-in-apis-django-rest-framework/)
- [@Django Rest Frameowrk](https://www.django-rest-framework.org/api-guide/pagination/)
- [@Code With Clinton - YouTube](https://www.youtube.com/watch?v=YyVj67CMJCw)
- [@Tech With Tim - YouTube](https://www.youtube.com/watch?v=t-uAgI-AUxc&t=931s)
- [@Stackoverflow](https://stackoverflow.com/questions/20239232/django-server-error-port-is-already-in-use)
- [@Yasodh Perera - Medium](https://yashodgayashan.medium.com/how-to-change-django-port-dbe55dbc7295)
- [@Caleb Curry - YouTube](https://www.youtube.com/watch?v=i5JykvxUk_A)
- [@Radix](https://radixweb.com/blog/create-rest-api-using-django-rest-framework)
- [@Log Rocket](https://blog.logrocket.com/django-rest-framework-create-api/)

