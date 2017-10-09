package Com.MS.CosmosDB.ex;

import org.apache.tinkerpop.gremlin.driver.Client;
import org.apache.tinkerpop.gremlin.driver.Cluster;

import org.apache.tinkerpop.gremlin.driver.Result;

import org.apache.tinkerpop.gremlin.driver.ResultSet;

import java.io.File;

import java.io.FileNotFoundException;

import java.util.List;

import java.util.concurrent.CompletableFuture;

import java.util.concurrent.ExecutionException;

public class App

{

	public static void main(String[] args) throws ExecutionException, InterruptedException {

		/**
		 * 
		 * There typically needs to be only one Cluster instance in an application.
		 * 
		 */

		Cluster cluster;
		 /**

         * Use the Cluster instance to construct different Client instances (e.g. one for sessionless communication

         * and one or more sessions). A sessionless Client should be thread-safe and typically no more than one is

         * needed unless there is some need to divide connection pools across multiple Client instances. In this case

         * there is just a single sessionless Client instance used for the entire App.

         */
		

		Client client;

		try {

			cluster = Cluster.build(new File("src/remote.yaml")).create();

		} catch (FileNotFoundException e) {

			e.printStackTrace();

			return;

		}

		client = cluster.connect();
		
		/*

        Example Gremlin queries to perform the following:

        - add vertices and edges

        - query with filters, projections, 

        - traversals, including loops

        - update annd delete vertices and edges

    */

		String gremlinQueries[] = new String[] {

				"g.V().drop()",

				"g.addV('person').property('id', 'mohan').property('firstName', 'Mohan').property('age', 44)",

				"g.addV('person').property('id', 'riya').property('firstName', 'Riya').property('lastName', 'Kumar').property('age', 39)",

				"g.addV('person').property('id', 'ram').property('firstName', 'Ram').property('lastName', 'singh')",

				"g.addV('person').property('id', 'rohan').property('firstName', 'Rohan').property('lastName', 'Das')" };

		for (String gremlin : gremlinQueries) {

			ResultSet results = client.submit(gremlin);

			CompletableFuture<List<Result>> completableFutureResults = results.all();

			List<Result> resultList = completableFutureResults.get();

			for (Result result : resultList) {

				System.out.println(result.toString());

			}

		}

	}

}
