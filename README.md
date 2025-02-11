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

## License

Copyright : Copyright 2023 AKKODIS

License : EUPL 1.2 ([https://eupl.eu/1.2/en/](https://eupl.eu/1.2/en/))

The European Union Public Licence (EUPL) is a copyleft free/open source software license created on the initiative of and approved by the European Commission in 23 official languages of the European Union.

Licensed under the EUPL License, Version 1.2 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at [https://eupl.eu/1.2/en/](https://eupl.eu/1.2/en/)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
