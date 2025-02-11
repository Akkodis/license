# 5GMETA Cloud Platform License API

This repository hosts the source code for the license API of the 5GMETA platform.

For the platform operator, the license API allows the management of the dataflow licenses to be made available to the data consumers i.e. creation, update and deletion.

For the data consumers, the license API allows to retrieve the available dataflow licenses.

## API Description
The yaml description of the APIs is available in [api](./api).    
   
- `GET /licenses` lists all the available licenses
- `GET /licenses/{license_id}` returns the details of a single license (for the platform operator only)
- `POST /licenses/{license_id}` creates a new license (for the platform operator only)
- `PUT /licenses/{license_id}` updates a license (for the platform operator only)
- `DELETE /licenses/{license_id}` deletes a license (for the platform operator only)

## Requirements

To use this module you will need:
* Python 3.5.2+
* PIP
* MongoDB

By default the module looks for its `license-data` database on the `mongodb://localhost:27017`

You can install the community edition of the MongoDB server following the [official instructions](https://www.mongodb.com/docs/manual/administration/install-community/). 

## Run
Once the requirements are fullfilled you can run the API with:

```
cd src/license-api
pip3 install -r requirements.txt
python3 -m swagger_server
```

## Container
To run the server on a Docker container, please execute the following:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 5000:5000 swagger_server
```

Running this container also require MongoDB on `mongodb://localhost:27017`

## Using the module
Once running you can access the swagger at 
```
http://localhost:5000/license-api/ui
```

## Credits

* Ricardo Benedetti
* Quentin Wephre
* Contact: 5gmeta@akkodis.com


