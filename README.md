
# triplestore-collaboration-descriptives

Vantage6 algorithm that retrieves the descriptive information of triplestores in a collaboration

This algorithm is designed to be run with the [vantage6](https://vantage6.ai)
infrastructure for distributed analysis and learning.

The base code for this algorithm has been created via the
[v6-algorithm-template](https://github.com/vantage6/v6-algorithm-template)
template generator.

### Dockerizing your algorithm

To finally run your algorithm on the vantage6 infrastructure, you need to
create a Docker image of your algorithm.

#### Automatically

The easiest way to create a Docker image is to use the GitHub Actions pipeline to
automatically build and push the Docker image. All that you need to do is push a
commit to the ``main`` branch.

#### Manually

A Docker image can be created by executing the following command in the root of your
algorithm directory:

```bash
docker build -t triplestore-collaboration-descriptives .
```

where you should provide a sensible value for the Docker image name. The
`docker build` command will create a Docker image that contains your algorithm.
You can create an additional tag for it by running

```bash
docker tag triplestore-collaboration-descriptives medicaldataworks.azurecr.io/projects/strongaya/triplestore-collaboration-descriptives
```

This way, you can e.g. do
`docker tag local_average_algorithm harbor2.vantage6.ai/algorithms/average` to
make the algorithm available on a remote Docker registry (in this case
`harbor2.vantage6.ai`).

Finally, you need to push the image to the Docker registry. This can be done
by running

```bash
docker push medicaldataworks.azurecr.io/projects/strongaya/triplestore-collaboration-descriptives
```

Note that you need to be logged in to the Docker registry before you can push
the image. You can do this by running `docker login` and providing your
credentials. Check [this page](https://docs.docker.com/get-started/04_sharing_app/)
For more details on sharing images on Docker Hub. If you are using a different
Docker registry, check the documentation of that registry and be sure that you
have sufficient permissions.