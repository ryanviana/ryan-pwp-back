import { IsString, IsNotEmpty, IsOptional } from 'class-validator';

export class CreateEducationDto {
  @IsString()
  @IsNotEmpty()
  degree: string;

  @IsString()
  @IsNotEmpty()
  institution: string;

  @IsString()
  @IsNotEmpty()
  startYear: string;

  @IsString()
  @IsNotEmpty()
  endYear: string;

  @IsString()
  @IsOptional()
  location?: string;

  @IsString()
  @IsOptional()
  description?: string;
}
