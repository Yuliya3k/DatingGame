## License
This project’s code is licensed under the [Creative Commons BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/).  
- ✍️ Attribution is required.  
- 🚫 Commercial use is not permitted.  
- 🔁 Derivatives must use the same license.  
- 🧠 Assets (graphics, models, etc.) are NOT included in this license.  

## Contributing Guidelines

1. Fork this repo.
2. Create a new branch for your feature or fix.
3. Commit your changes with clear messages.
4. Open a Pull Request to the `contributors` branch.
5. All contributions must follow the CC BY-NC-SA 4.0 license.
6. Commercial use is not allowed — you must credit the original author (Yuliya3k) in any forks or derived works.
7. Permitted Use: This code may be used in non-commercial academic or medical research projects, provided attribution is given and no profit is generated from its use.


Copyright (c) 2025 Yuliya3k


## Event Scheduling

Use `schedule_event(day, hour, label, conditions=None)` to queue events that
should run at a specific in‑game time. `conditions` is a list of variable/value
pairs that must all match for the event to trigger.

Example:

```
schedule_event(calendar.TotalDays + 1, 9, "morning_call",
               [("goal_aurora", "Reach out for support")])
```

