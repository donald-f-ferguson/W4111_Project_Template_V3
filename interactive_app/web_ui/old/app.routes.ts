import { Routes } from '@angular/router';
import { TeamComponent } from './teams/teams.component';

export const routes: Routes = [
  // Go to team component by default
  {
    path: '',
    component: TeamComponent
  }
];
