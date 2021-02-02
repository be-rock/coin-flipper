# coin-flipper

An implementation of a coin flipper as suggested by...

>https://github.com/karan/Projects
>
> Coin Flip Simulation - Write some code that simulates flipping a single 
>coin however many times the user decides. The code should record the 
>outcomes and count the number of tails and heads.

...with influences from:

- the (excellent) [Architecture Patterns with Python book](https://www.cosmicpython.com/#buy_the_book)
- [Onion Architecture](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/)
- [Hexagonal / Ports and Adapters Architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software))
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

## App Purpose

Given a simple domain (coin flip), apply principles of TDD, DDD, and the above architectures.

## App Components

- [X] Coin Flipper REST API
- [X] Event-Driven Architecture
- [X] Database Integration (Repository Pattern)
- [X] Domain Model

## How to run

The app can be initiated with the provided:

```shell
scripts/run_app.sh
```

Once the API is up and running, swagger docs can be accessed
from:

`http://hostname/port/docs`

Where `hostname` and `port` are specified in environment variables
or overridden in `scripts/run_app.sh`


## Todo 

- [ ] coinflip api /results/{flipid}
- [ ] precommit integration
- [ ] unit of work pattern
- [ ] docker
- [ ] 100% test coverage
- [ ] logger decorator
- [ ] https
- [ ] http basic auth
- [ ] paginated api
- [ ] Coin Flipper CLI (typer? golang?)
