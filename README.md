# coin-flipper

[![Build Status](https://travis-ci.com/be-rock/coin-flipper.svg?branch=main)](https://travis-ci.com/be-rock/coin-flipper)
[![codecov.io](https://codecov.io/github/be-rock/coin-flipper/coverage.svg?branch=main)](https://codecov.io/github/be-rock/coin-flipper?branch=main)

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

- [X] Domain Model
- [X] Event-Driven Architecture
- [X] Coin Flipper REST API
- [X] Database Integration (Repository Pattern)
- [X] 100% Test Coverage

## How to run

The app can be initiated with the provided:

```shell
scripts/run_app.sh
```

Once the API is up and running, swagger docs can be accessed
from:

[http://localhost/8080/docs](http://localhost/8080/docs)

## Todo

- [ ] coinflip api /results/{flipid}
- [ ] paginated api results
- [ ] proper CQRS
- [ ] precommit integration
- [ ] docker
- [ ] logger decorator
- [ ] https
- [ ] http basic auth
- [ ] Coin Flipper CLI (typer? golang?)
- [ ] github automatic test integration
