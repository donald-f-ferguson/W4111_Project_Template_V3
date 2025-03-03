import { Routes } from '@angular/router';
import { ArtistComponent } from './Artist/artist.component';

export const routes: Routes = [
  // Go to team component by default
  {
    path: '',
    component: ArtistComponent
  }
];
