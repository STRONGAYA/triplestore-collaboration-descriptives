"""
This module contains the central part of the algorithm for the triplestore collaboration descriptives.

The `central` function creates a task for all organisations in the collaboration to fetch their sample size and
FAIRification information.
It waits for the results and returns them in a dictionary format.

Functions:
    central(client: AlgorithmClient) -> Any: Executes the central part of the algorithm.
"""
from typing import Any
from vantage6.algorithm.tools.util import info, error
from vantage6.algorithm.tools.decorators import algorithm_client
from vantage6.algorithm.client import AlgorithmClient


@algorithm_client
def central(client: AlgorithmClient) -> Any:
    """
    Executes the central part of the algorithm for the collaboration descriptives.

    This function creates a task for all organisations in a collaboration to then fetch their sample size and
    FAIRification information.
    It waits for the results and returns them in a dictionary format.

    Args:
        client (AlgorithmClient): The client instance for the algorithm.

    Returns:
        dict: A dictionary containing the organisation name, sample size, and FAIRification information.
    """
    # Get the ids of all organisations
    org_ids = [org.get("id") for org in client.organization.list()]
    org_names = [org.get("name") for org in client.organization.list()]

    # Create a task for all organisations to fetch their sample size and FAIRification information
    info("Creating a partial task for all organizations.")
    try:
        task = client.task.create(
            input_={"method": "partial"},
            organizations=org_ids,
            name="Organisation descriptives",
            description="Fetches organisation's sample size and FAIRification information"
        )
    except Exception as e:
        error(f"Unknown error occurred when creating partial tasks, error: {e}.")
        return f"Unknown error occurred when creating partial tasks, error: {e}."

    info("Waiting for the partial tasks to return their result.")
    # Wait for the results
    _results = client.wait_for_results(task_id=task.get("id"))

    info("Partial results received.")

    # If no results were returned, log an error and return an empty dictionary
    if not _results:
        error("All partial results returned empty and partial tasks might have failed, check node logs.")
        return "All partial results returned empty and partial tasks might have failed, check node logs."

    try:
        # Create a dictionary with the organisation name, sample size, and FAIRification information
        results = {res['organisation']: {"sample_size": res['sample_size'], "variable_info": res['variable_info']}
                   for res in _results}

        # Add any missing organisations to the results dictionary
        results = {org_name: results.get(org_name, "missing") for org_name in org_names}
    except Exception as e:
        error(f"Unknown error occurred when combining results, error: {e}.")
        return f"Unknown error occurred when combining results, error: {e}."

    return results
