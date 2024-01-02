# eindproject-api-development-videogames
In dit document ga ik screenshots tonen van mijn API voor het basisproject, om aan te tonen dat deze API ook degelijk werkt.ames te verkrijgen en deze in deze API en database te verwerken.
Mijn gekozen thema is videogames. Deze API kan worden gebruikt om een eigen bibliotheek van games bij te houden, evenals bijbehorende informatie zoals de ontwikkelaars en platformen waarop deze gespeeld kunnen worden.
In de toekomst kan de API worden uitgebreid om mogelijk informatie van openbare API's van Steam of Epic Games te verkrijgen en deze in deze API en database te verwerken.


## Features
In deze tab ga ik uitleggen wat mijn API kan.
- GET endpoints op de tabellen videogames, genres, platformen en ontwikkelaars. Deze kunnen ook via een specifieke id opgeroepen worden voor als je bv. een specifiek record wilt hebben.
- POST endpoints op de tabellen videogames, genres, platformen en ontwikkelaars. Deze kunnen in BULK gedaan worden via een lijst.
- PUT endpoints op alle tabellen met een POST endpoint
- DELETE endpoints op de tabellen videogames, genres, platformen en ontwikkelaars. Records kunnen specifiek verwijderd wordne met hun id
- Authenticatie op de DELETE endpoints via basic auth.
- Mariadb als databank met volumes gedefinieerd in docker voor persistentie.




## Screenshots
### OpenAPI Docs:

##### GET videogames:
![GET_videogames_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/f0079ea7-55b8-49f3-8ace-7b12cb6e228c)
![GET_videogames_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/f375b8ae-76fe-4abb-8c18-cefa2cb9c3b7)
![GET_videogames_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/45c85ca7-0942-4ca9-be29-3090219ca024)

##### GET videogames by id:
![GET_videogames_by_id_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/370b4dac-331d-4b51-b7da-2884955ff099)
![GET_videogames_by_id_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/101f1f19-0df0-4720-bac5-37b859ba1f2c)
![GET_videogames_by_id_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/c54ab32a-72cf-41e4-942f-abe83c19e553)

##### POST videogames:
![POST_videogames_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/eaed2f76-8d8b-4509-ada5-1b73528ec053)
![POST_videogames_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/e1236e39-b11e-431a-99a8-cb0e8534cc07)
![POST_videogames_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/dfefcf21-1d03-417c-bbbb-ee9144c4283f)

##### DELETE videogames by id:
![DELETE_videogames_by_id_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/dd7d7045-6707-48fe-b405-3cb93166537d)
![DELETE_videogames_by_id_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/68fe0b20-fb5d-4d78-a24c-4c713eb3a1eb)
![DELETE_videogames_by_id_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/d7ee071e-132b-4772-9ce5-aabe416bf3ac)

##### PUT videogames by id:
![Screenshot 2024-01-02 at 22-28-43 FastAPI - Swagger UI](https://github.com/r0901651/eindproject-api-development-videogames/assets/95848828/b8a844bc-90c8-4ff5-ba5b-6db2b6969fb8)



##### GET genres:
![GET_genres_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/5e946fae-b65d-4944-bffe-f806b1e6f1d0)
![GET_genres_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/3e0158bf-9e22-495b-a8ff-14e552675b0e)
![GET_genres_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/c1acae71-7c77-45ce-b26d-d891641cbdc7)

##### GET genres by id:
![GET_genres_by_id_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/3d5154e3-cd86-4546-9863-20e6fce38c18)
![GET_genres_by_id_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/ffb07f8f-b6ca-4552-bb34-7075149d9fc1)
![GET_genres_by_id_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/ec3283c0-3e2a-41fa-aedb-6fec62f0e458)

##### POST genres:
![POST_genres_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/1677cf6d-04bf-4b62-b5d7-a0ba36e13c32)
![POST_genres_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/838ba4a5-2880-42c7-a015-aedc73ae8199)
![POST_genres_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/872b0be9-5421-4a7a-81e1-b89a3bd9bd08)

##### DELETE genres by id:
![DELETE_genres_by_id_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/1ac10eaa-ad00-4dec-b45f-5af53e541ec4)
![DELETE_genres_by_id_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/153d6ebc-c706-4091-bd4b-ff469e218686)
![DELETE_genres_by_id_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/8ecc07c1-e25e-4e28-b44e-7a711d6e5a71)

##### PUT genres by id:
![Screenshot 2024-01-02 at 22-29-01 FastAPI - Swagger UI](https://github.com/r0901651/eindproject-api-development-videogames/assets/95848828/5f381bcc-3061-429a-b300-ba53ea5400b0)



##### GET ontwikkelaars:
![GET_ontwikkelaars_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/53db7c15-921d-4275-8238-262c2f99a293)
![GET_ontwikkelaars_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/f23491c5-a354-44ab-8a74-cd40dd4d87c4)
![GET_ontwikkelaars_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/f6217d27-74d7-44f2-9ba8-833a5a92f426)

##### GET ontwikkelaars by id:
![GET_ontwikkelaars_by_id_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/9d450e56-7f1b-4578-8d6e-d276eedb7c1a)
![GET_ontwikkelaars_by_id_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/040f2571-cf1c-4bd4-b3f6-28c85a8582a4)
![GET_ontwikkelaars_by_id_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/b5188bf5-0927-4d89-800e-7568b41fd225)

##### POST ontwikkelaars:
![POST_ontwikkelaars_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/dbc27781-2384-4880-a890-e4ae965fbc84)
![POST_ontwikkelaars_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/402c5c49-1e76-497b-9d5d-ca99f136a7f8)
![POST_ontwikkelaars_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/24bb719d-93ff-4d5f-b8fc-694a3c8ed391)

##### DELETE ontwikkelaars by id:
![DELETE_ontwikkelaars_by_id_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/337143e9-a847-42b2-8f44-914e2d264832)
![DELETE_ontwikkelaars_by_id_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/1e45d4c6-6bf8-4886-9e5e-0c1a978edfa7)
![DELETE_ontwikkelaars_by_id_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/5562ad4d-a98e-470b-a94b-c6ab8a042abe)

##### PUT ontwikkelaars by id:
![Screenshot 2024-01-02 at 22-29-14 FastAPI - Swagger UI](https://github.com/r0901651/eindproject-api-development-videogames/assets/95848828/13c9c16c-103d-4066-bb4b-b412ceb5647a)



##### GET platformen:
![GET_platformen_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/6ebfb9a3-d887-400a-900a-374366545984)
![GET_platformen_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/a0f327ff-2207-40fd-801d-69133817cab5)
![GET_platformen_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/3c685d01-b39c-4239-8eee-31fb5939a16d)

##### GET platformen by id:
![GET_platformen_by_id_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/f122b382-65a2-4505-850b-7fa7abe3800f)
![GET_platformen_by_id_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/c764af7e-8632-4cdd-af4c-5a033d850284)
![GET_platformen_by_id_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/5588794d-5090-477d-843e-179494cbb22b)

##### POST platformen:
![POST_platformen_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/73297f40-db30-48ff-bcce-55d2e560e9e9)
![POST_platformen_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/0f47bd00-4cb0-4175-95f0-afc65150b655)
![POST_platformen_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/22775098-62a3-4bfa-b19e-b60e30a092e3)

##### DELETE platformen by id:
![DELETE_platformen_by_id_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/97f9ccf8-9d10-4048-a44e-f3dff6e96576)
![DELETE_platformen_by_id_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/d4428f38-2fc7-42cf-8f9c-313edeebae0e)
![DELETE_platformen_by_id_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/63572eae-4236-47cc-b494-47f1651eba39)

##### PUT platformen by id:
![Screenshot 2024-01-02 at 22-29-29 FastAPI - Swagger UI](https://github.com/r0901651/eindproject-api-development-videogames/assets/95848828/b591f853-a74c-458e-8751-e83f9471b9bb)




### Postman:

##### GET request van alle tabellen zonder data:
![Empty_GET_platformen](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/fac38bed-99e0-4b3b-8342-340bb83607cf)
![Empty_GET_ontwikkelaars](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/083f92c8-e34d-4d27-a967-828f159bfb16)
![Empty_GET_genres](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/6891cacd-6df8-4362-856e-2231da3c0fdd)
![Empty_GET_videogames](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/5f9c7e21-dd42-4937-8b2b-9821f7aac70e)



##### PUT request naar genres:
![PUT_meerdere_genres](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/0a895eeb-e578-454b-becd-7aab5226168f)
![PUT_enkele_genres](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/a6901185-a920-4cad-8f23-755c047c6f54)



##### GET request na PUT van genres:
![GET_genres_na_PUT](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/4f4651ed-59a1-42ac-9c28-a78ae110982a)



##### PUT request naar platformen:
![PUT_platformen](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/cad9cb2b-2642-4584-9995-77443a94e88f)



##### GET request na PUT van platformen:
![GET_platformen_na_PUT](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/b111d448-a27b-4199-8128-0841f5752db2)



##### PUT request ontwikkelaars:
![PUT_ontwikkelaars](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/fbdf4753-4589-4a19-8fb9-237f3c3362f4)



##### GET request na PUT van ontwikkelaars:
![GET_ontwikkelaars_na_PUT](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/654fb187-d993-4bfe-bf11-8cba7a173d4e)



##### PUT request videogames:
![PUT_videogames](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/6e436a2c-8264-4309-93dc-3c5e1f4e0c7e)



##### GET request na PUT van videogames:
![GET_videogames_na_PUT](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/137ed778-68bc-4d50-a511-80ceadff68a1)



##### GET request via id van videogames:
![GET_by_id_videogames](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/eacdfeca-15fd-4b54-8a0e-a63126ddb0a0)



##### DELETE request via id zonder authorization:
![DELETE_videogame_by_id_no_auth](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/cc45965a-4181-41cf-bd9b-b656fd79a40d)




##### DELETE request via id videogames met authorization:
![DELETE_videogame_by_id_auth_01](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/ccb9d15a-3b74-44c3-9e1a-c42445033176)
![DELETE_videogame_by_id_auth_02](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/4728d2dd-1307-4a5d-bd0c-1aba0c552994)
![DELETE_videogame_by_id_auth_03](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/2b507731-dadf-46aa-948d-7cd4075f1a1c)
![DELETE_videogame_by_id_auth_04](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/d121c022-35a9-47c9-8da5-9da2bac3d8f4)





### Okteto:
![Octeto](https://github.com/r0901651/basisproject-api-development-videogames/assets/95848828/e146424b-3b3a-484a-ac75-eea43fe5f80a)


### API testing workflow:
![Screenshot 2024-01-02 at 22-33-59 changed readme · r0901651_eindproject-api-development-videogames@6e93e84](https://github.com/r0901651/eindproject-api-development-videogames/assets/95848828/6355c8ca-0a0d-47f7-bca4-ae9ffd045bb1)
