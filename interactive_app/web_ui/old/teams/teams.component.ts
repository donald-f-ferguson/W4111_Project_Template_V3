import { Component, OnInit } from '@angular/core';
import { TeamService, Team } from '../services/team.service';  // Make sure the service path is correct
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';  // Import CommonModule for *ngFor and *ngIf

@Component({
  selector: 'app-team',  // The selector is optional here as we're bootstrapping it directly
  standalone: true,  // Standalone component
  // you can optimize the imports by using NgIf and NgFor imports directly (or use the new control flow syntax)
  imports: [FormsModule, CommonModule],  // Add CommonModule here for *ngFor and *ngIf
  templateUrl: './teams.component.html',  // Ensure this points to your actual HTML file
})
export class TeamComponent implements OnInit {
  teams: Team[] = [];  // Array to hold the list of Artist
  newTeam: Team = { id: 0, name: '', description: '' };  // For creating a new team
  selectedTeam: Team | null = null;  // Property to hold the selected team for editing

  constructor(private teamService: TeamService) {}

  ngOnInit(): void {
    this.loadTeams();
  }

  loadTeams(): void {
    this.teamService.getTeams().subscribe((data: Team[]) => {
      this.teams = data;
    });
  }

  createTeam(): void {
    this.teamService.createTeam(this.newTeam).subscribe((team: Team) => {
      this.teams.push(team);
      this.newTeam = { id: 0, name: '', description: '' };  // Reset form
    });
  }

  editTeam(team: Team): void {
    this.selectedTeam = { ...team };  // Create a copy of the team to edit
  }

  updateTeam(): void {
    if (this.selectedTeam) {
      this.teamService.updateTeam(this.selectedTeam.id, this.selectedTeam).subscribe(() => {
        this.loadTeams();  // Refresh the team list
        this.selectedTeam = null;  // Clear the selected team after update
      });
    }
  }

  deleteTeam(id: number): void {
    this.teamService.deleteTeam(id).subscribe(() => {
      this.teams = this.teams.filter(t => t.id !== id);  // Remove the deleted team from the list
    });
  }
}
