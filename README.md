
# Overview

This is a small sample to demonstrate how to simulate data for ingestion into
Predix Time Series Service.

# Requirements

- [ ] You must have at minimum a [Predix Free Tier](signup) account.
- [ ] You must have the [Cloud Foundry CLI](cf) and can run `cf login`
- [ ] You will need PredixPy in your python environment `pip install predix`

# Setup

## Workspace

To keep things tidy, you can create a dedicated workspace for this project
within your cloud foundry organization.

- [ ] Create a new space to target this project

```
cf create-space voltaged
cf target -s voltaged
```

## Services

To simulate data, you need UAA for client authentication and tenancy id for the
Time Series service.

- [ ] Create UAA and TimeSeries service instances

There is a sample script that can automate this for you.  Take a look at it and
then run it:

```
python setup_space.py
```

## Simulation

This is the reason you came here afterall.  You can just run the simulator.py
and some example tags and values will be generated at the frequency you want
(or your hardware supports).

```
python simulator.py
```

Need more input?  You can use the `threading` library but that is left as an
exercise for the reader.

## Cleanup

You should put away your toys when done so that you don't leave orphan services
or an unused space sitting around.

- [ ] Delete services and remove space

I created a script to help with this as well -- but be careful since this will
*permanently delete all services in your target space.*
```
python delete_all_the_things.py
```

---
[signup]: https://www.predix.io/registration
[cf]: https://github.com/cloudfoundry/cli
