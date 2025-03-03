import { Component, OnInit } from '@angular/core';
import { ArtistService, Artist, ArtistRsp } from '../services/artist.service';  // Make sure the service path is correct
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';  // Import CommonModule for *ngFor and *ngIf

@Component({
  selector: 'app-artist',  // The selector is optional here as we're bootstrapping it directly
  standalone: true,  // Standalone component
  // you can optimize the imports by using NgIf and NgFor imports directly (or use the new control flow syntax)
  imports: [FormsModule, CommonModule],  // Add CommonModule here for *ngFor and *ngIf
  templateUrl: './artist.component.html',  // Ensure this points to your actual HTML file
})
export class ArtistComponent implements OnInit {
  Artists: ArtistRsp[] = [];  // Array to hold the list of Artist
  currentArtist: Artist = { nconst: "",
    first_name: "", middle_name: "", last_name: "", title: "",
    suffix: "", nickname: "", birth_year: "", death_year: ""};
  newArtist: Artist = { nconst: "",
    first_name: "", middle_name: "", last_name: "", title: "",
    suffix: "", nickname: "", birth_year: "", death_year: ""};  // For creating a new Artist
  selectedArtist: Artist | null = null;  // Property to hold the selected Artist for editing

  people = [
    { title: 'Dr.', firstName: 'John', middleName: 'A.', lastName: 'Doe', suffix: 'Jr.', nickname: 'Johnny', nconst: 'nm0000123' },
    { title: 'Ms.', firstName: 'Jane', middleName: 'B.', lastName: 'Smith', suffix: '', nickname: 'Janey', nconst: 'nm0000456' },
    { title: 'Mr.', firstName: 'Robert', middleName: '', lastName: 'Brown', suffix: 'Sr.', nickname: '', nconst: 'nm0000789' },
    { title: '', firstName: 'Alice', middleName: 'C.', lastName: 'Johnson', suffix: '', nickname: 'Ali', nconst: 'nm0000999' }
  ];

  constructor(private ArtistService: ArtistService) {}

  ngOnInit(): void {
    // this.loadArtists();
    this.people = this.people;
  }

  loadArtists(): void {
    this.ArtistService.getArtists().subscribe((data: ArtistRsp[]) => {
      this.Artists = data;
    });
  }

  getArtist(): void {
    this.ArtistService.getArtistById(this.currentArtist.nconst).subscribe((data: ArtistRsp) => {
      this.currentArtist = data.data;
    });
  }

  createArtist(): void {
    this.ArtistService.createArtist(this.newArtist).subscribe((artistRsp: ArtistRsp) => {
      this.Artists.push(artistRsp);
      this.newArtist = artistRsp.data;  // Reset form
    });
  }

  editArtist(Artist: Artist): void {
    this.selectedArtist = { ...Artist };  // Create a copy of the Artist to edit
  }

  updateArtist(): void {
    if (this.selectedArtist) {
      this.ArtistService.updateArtist(this.selectedArtist.nconst, this.selectedArtist).subscribe(() => {
        this.loadArtists();  // Refresh the Artist list
        this.selectedArtist = null;  // Clear the selected Artist after update
      });
    }
  }

  deleteArtist(id: string): void {
    this.ArtistService.deleteArtist(id).subscribe(() => {
      this.Artists = this.Artists.filter(t => t.data.nconst !== id);  // Remove the deleted Artist from the list
    });
  }
}
