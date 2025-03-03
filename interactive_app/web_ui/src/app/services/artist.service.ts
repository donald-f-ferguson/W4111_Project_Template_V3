import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface ArtistRsp {
  data: Artist
  links: Link[]
}

export interface Artist {
  nconst: string
  title: any
  first_name: string
  middle_name: any
  last_name: string
  suffix: any
  nickname: any
  birth_year: string
  death_year: string
}

export interface Link {
  rel: string
  href: string
}

@Injectable({
  providedIn: 'root'  // Makes this service available throughout the application
})
export class ArtistService {

  private apiUrl = 'http://localhost:8001/api/artists';  // Replace with your API URL

  constructor(private http: HttpClient) { }

  // GET: Retrieve a single team by ID
  getArtistById(id: string): Observable<ArtistRsp> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.get<ArtistRsp>(url);
  }

  // GET: Retrieve a single team by ID
  getArtists(): Observable<ArtistRsp[]> {
    const url = `${this.apiUrl}`;
    return this.http.get<ArtistRsp[]>(url);
  }


  // POST: Create a new team
  createArtist(artist: Artist): Observable<ArtistRsp> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<ArtistRsp>(this.apiUrl, artist, { headers });
  }

  // PUT: Update an existing team by ID
  updateArtist(id: string, artist: Artist): Observable<ArtistRsp> {
    const url = `${this.apiUrl}/${id}`;
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.put<ArtistRsp>(url, artist, { headers });
  }

  // DELETE: Delete a team by ID
  deleteArtist(id: string): Observable<void> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.delete<void>(url);
  }
}
