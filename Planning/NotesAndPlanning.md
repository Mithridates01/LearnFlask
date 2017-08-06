*Initial thoughts and planning

** User Stories
  - As a student I log arrive on site
  - As a student I Click register for classes
  - As a student I must choose one english, math, science, history, and elective class
    - A class type has Periods
      - A class can have multiple classes
    - Periods have times
    - When one period is taken for a specific class, all other classes will not have that period as an available period.



  ** Notes:
    *** Problems
      This will be a simple MVP and will have many issue that will cause    significant refactoring down the road.
        - Schools have differing number of periods that differ in time amount. For simplicity I am making all schools have stand set of periods.
        -
    *** Architecture decisions
      - Python 3 used for increase future proofing and additional features. Assumption is that I am starting out not in an existing Python > 3 code base
      - 