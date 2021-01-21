# coin-flipper

An implementation of a coin flipper as suggested by...

>https://github.com/karan/Projects
>
> Coin Flip Simulation - Write some code that simulates flipping a single 
>coin however many times the user decides. The code should record the 
>outcomes and count the number of tails and heads.

...with influences from the [Architecture Patterns with Python book](https://www.cosmicpython.com/#buy_the_book). 

## App Components:

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

- [ ] versioned api / routers
- [ ] coinflip api /results/{flipid}
- [ ] precommit integration
- [ ] unit of work pattern
- [ ] docker
- [ ] 100% test coverage
- [ ] logger decorator
- [ ] https
- [ ] http basic auth
- [ ] Coin Flipper CLI
