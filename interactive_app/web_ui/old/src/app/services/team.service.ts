import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Team {
  id: number;
  name: string;
  description: string;
}

@Injectable({
  providedIn: 'root'  // Makes this service available throughout the application
})
export class TeamService {

  private apiUrl = 'http://localhost:8000/teams';  // Replace with your API URL

  constructor(private http: HttpClient) { }

  // GET: Retrieve all Artist
  getTeams(): Observable<Team[]> {
    return this.http.get<Team[]>(this.apiUrl);
  }

  // GET: Retrieve a single team by ID
  getTeamById(id: number): Observable<Team> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.get<Team>(url);
  }

  // POST: Create a new team
  createTeam(team: Team): Observable<Team> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<Team>(this.apiUrl, team, { headers });
  }

  // PUT: Update an existing team by ID
  updateTeam(id: number, team: Team): Observable<Team> {
    const url = `${this.apiUrl}/${id}`;
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.put<Team>(url, team, { headers });
  }

  // DELETE: Delete a team by ID
  deleteTeam(id: number): Observable<void> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.delete<void>(url);
  }
}
