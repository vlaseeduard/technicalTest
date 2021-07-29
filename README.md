# technicalTest


Simple Django application and a Postgres database.
It creates a simple TODO application.

A staff user chooses the location of the task when creating/updating a task and, using the location data, the system retrieves the current weather
(using https://openweathermap.org/api) and changes the background colour of the task. Blue for “cold” or “rain”, Yellow-Orange for “warm” or
“cloudy” and Red for “hot” or “sunny” purple.

-When a task is marked as done, the task records the latest temperature but no longer updates it in real time.
